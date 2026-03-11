import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Optional, Tuple

from deepseek_infer import get_response

# 可重试的错误关键词（连接、超时等瞬时故障）
RETRY_KEYWORDS = ("connection", "timeout", "connect", "network", "reset", "refused")
MAX_RETRIES = 3
INITIAL_BACKOFF = 2.0  # 秒


def build_response(content: str, reasoning_content: Optional[str]) -> str:
    """
    将 reasoning_content 包裹为 <think></think>，并与最终回答合并为一个 response 字段。
    """
    if reasoning_content:
        return f"<think>{reasoning_content}</think>\n{content}"
    return content


def _is_retryable_error(e: Exception) -> bool:
    """判断是否为可重试的瞬时错误（连接、超时等）。"""
    msg = str(e).lower()
    return any(kw in msg for kw in RETRY_KEYWORDS)


def _process_one(
    index: int,
    instruction: str,
    system_prompt: str,
    model_name: str,
) -> Tuple[int, dict[str, Any]]:
    """
    处理单条数据。返回 (原始序号, 输出对象)。
    - 成功时：{"instruction": ..., "response": "..."}
    - 失败时：{"instruction": ..., "response": None, "error": "错误信息", "error_type": "异常类名"}
    对连接/超时类错误自动重试最多 MAX_RETRIES 次（指数退避）。
    """
    last_error: Optional[Exception] = None
    backoff = INITIAL_BACKOFF

    for attempt in range(MAX_RETRIES + 1):
        try:
            content, reasoning_content = get_response(
                system_content=system_prompt,
                user_content=instruction,
                model_name=model_name,
                timeout=600
            )
            response = build_response(content, reasoning_content)
            return (index, {"instruction": instruction, "response": response})
        except Exception as e:
            last_error = e
            if attempt < MAX_RETRIES and _is_retryable_error(e):
                wait = backoff * (2 ** attempt)
                print(f"[重试] 第 {index + 1} 条第 {attempt + 1} 次失败 ({e})，{wait:.0f}s 后重试...")
                time.sleep(wait)
            else:
                print(f"[警告] 处理第 {index + 1} 条失败: {e}")
                return (
                    index,
                    {
                        "instruction": instruction,
                        "response": None,
                        "error": str(e),
                        "error_type": type(e).__name__,
                    },
                )

    print(f"[警告] 处理第 {index + 1} 条失败（已重试 {MAX_RETRIES} 次）: {last_error}")
    return (
        index,
        {
            "instruction": instruction,
            "response": None,
            "error": str(last_error),
            "error_type": type(last_error).__name__ if last_error else "UnknownError",
        },
    )


def process_jsonl(
    input_path: str,
    output_path: str,
    system_prompt: str = "请根据用户的指令给出清晰、完整的回答。",
    model_name: str = "DeepSeek-R1-0528",
    max_workers: int = 10,
) -> None:
    """
    从 input_path 读取 jsonl，每行取 instruction 字段作为 prompt，
    多线程调用大模型，并将 {instruction, response} 按输入顺序写入 output_path（jsonl）。
    response 字段中包含 <think>reasoning_content</think> 和最终回答。
    max_workers 控制同时进行中的请求数，避免一次性提交全部数据导致并发过高。
    """
    import os
    if not os.path.isfile(input_path):
        print(f"[错误] 输入文件不存在: {input_path}")
        return

    # 读取并解析，只保留有 instruction 的行，带原始序号
    items: list[Tuple[int, str, str, str]] = []
    with open(input_path, "r", encoding="utf-8") as fin:
        for i, line in enumerate(fin):
            line = line.strip()
            if not line:
                continue
            data = json.loads(line)
            instruction = data.get("instruction")
            if not instruction:
                continue
            items.append((i, instruction, system_prompt, model_name))

    if not items:
        print(f"[警告] {input_path} 中没有有效的 instruction 行，未生成输出。")
        return

    print(f"[进度] 共 {len(items)} 条，并发数 max_workers={max_workers}，结果将实时写入 {output_path}")

    # 多线程处理：只保持最多 max_workers 个在途任务，完成一个再提交下一个，避免一次性提交全部
    next_to_write = 0
    pending: dict[int, dict[str, Any]] = {}
    items_iter = iter(items)
    total = len(items)
    success_count = 0
    failure_count = 0

    def submit_next():
        try:
            (idx, inst, sys_p, mod) = next(items_iter)
            return executor.submit(_process_one, idx, inst, sys_p, mod), idx
        except StopIteration:
            return None, None

    with open(output_path, "w", encoding="utf-8") as fout:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_index: dict = {}
            # 先提交一批，数量不超过 max_workers
            for _ in range(max_workers):
                fut_idx = submit_next()
                if fut_idx[0] is None:
                    break
                fut, idx = fut_idx
                future_to_index[fut] = idx

            done_count = 0
            while future_to_index:
                for future in as_completed(future_to_index):
                    index, out_obj = future.result()
                    done_count += 1

                    # 统计成功 / 失败数
                    if isinstance(out_obj, dict) and (
                        "error" in out_obj or out_obj.get("response") is None
                    ):
                        failure_count += 1
                    else:
                        success_count += 1

                    if done_count % 5 == 0 or done_count == total:
                        print(
                            f"[进度] 已完成 {done_count}/{total} 条（成功 {success_count} 条，失败 {failure_count} 条）"
                        )

                    # 无论成功或失败，都暂存到 pending，以保证按原始顺序处理
                    pending[index] = out_obj
                    # 按原始顺序连续写出能连上的部分
                    while next_to_write in pending:
                        obj = pending.pop(next_to_write)
                        # 仅当 response 不为 None 时才写入输出文件
                        if obj.get("response") is not None:
                            fout.write(json.dumps(obj, ensure_ascii=False) + "\n")
                            fout.flush()
                        next_to_write += 1
                    # 完成一个就再提交一个，保持并发数受控
                    del future_to_index[future]
                    new_fut, new_idx = submit_next()
                    if new_fut is not None:
                        future_to_index[new_fut] = new_idx
                    break  # 只处理一个完成的任务，再循环 as_completed

        # 若有因顺序未处理完的，按序补写（同样只写入 response 不为 None 的结果）
        for idx in sorted(pending.keys()):
            obj = pending[idx]
            if obj.get("response") is not None:
                fout.write(json.dumps(obj, ensure_ascii=False) + "\n")
                fout.flush()
        print(f"[完成] 已写入 {output_path}")


if __name__ == "__main__":
    # 默认读取当前目录下的 instruction.jsonl，输出到 distill_QA.jsonl
    # max_workers：同时进行中的请求数，可按 API 限流或机器能力调整（如 2、4、8）
    process_jsonl(
        input_path="instruction.jsonl",
        output_path="distill_QA.jsonl"
    )

