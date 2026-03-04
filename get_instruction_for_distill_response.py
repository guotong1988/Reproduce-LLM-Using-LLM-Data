# capability x domain x difficulty

capability = {}

capability["通用对话"] = [
    "闲聊",
    "情感陪伴",
    "角色扮演",
    "日常问候",
    "观点讨论",
    "冲突化解",
    "建议与决策陪伴",
]
capability["知识问答"] = [
    "事实性查询",
    "百科知识",
    "概念解释",
    "定义辨析",
    "历史事件问答",
    "数据与统计解读",
    "背景信息补充",
]
capability["内容创作"] = [
    "写作",
    "邮件",
    "文案",
    "诗歌",
    "剧本",
    "报告撰写",
    "演讲稿",
    "社交媒体内容",
    "课程大纲与教学设计",
]
capability["逻辑推理"] = [
    "数学",
    "科学推理",
    "常识推理",
    "归纳推理",
    "演绎推理",
    "反事实推理",
    "题目步骤拆解",
    "谜题与逻辑游戏",
]
capability["代码技术"] = [
    "编写",
    "调试",
    "解释",
    "SQL",
    "Shell",
    "代码优化",
    "重构",
    "单元测试编写",
    "API 设计",
    "代码审查与建议",
]
capability["长文本处理"] = [
    "摘要",
    "提取",
    "长文档问答",
    "结构化重写",
    "关键信息对比",
    "多文档信息汇总",
    "思维导图与提纲生成",
]
capability["多模态/工具"] = [
    "调用API",
    "画图指令",
    "表格处理",
    "文件解析",
    "浏览器或搜索工具调用",
    "日程与待办管理工具",
]

domain = {}
domain["基础学科"] = ["文学", "历史", "哲学", "数学", "物理", "化学", "生物", "地理", "计算机基础", "逻辑学"]
domain["垂直专业"] = ["医疗", "法律", "金融", "教育", "心理学", "新闻传媒", "管理学"]
domain["生活服务"] = ["旅游", "餐饮", "购物", "家政", "交通出行", "健康养生", "亲子育儿"]
domain["工程技术"] = ["机械", "建筑", "电子", "化工", "土木", "自动化", "材料", "航空航天", "海洋工程", "能源与环保"]
domain["互联网/IT"] = ["产品", "运营", "开发", "数据", "安全", "测试", "运维"]
domain["政务/公文"] = ["政策解读", "公文写作", "政府服务", "会议纪要", "通知公告"]

difficulty = {}
difficulty["Level-1"] = ["简单指令，单轮对话"]
difficulty["Level-2"] = ["复杂指令，需要多步推理"]
difficulty["Level-3"] = ["专家级任务"]

import json
import time
from typing import Dict, Any
from concurrent.futures import ThreadPoolExecutor, as_completed

from deepseek_infer import get_response


def build_user_prompt(
    cap_key: str,
    cap_item: str,
    dom_key: str,
    dom_item: str,
    diff_key: str,
) -> str:
    """
    根据能力 / 领域 / 难度构造给大模型的提示词，
    让大模型只返回一条「用户指令 / prompt」的 JSON。
    其中每条指令只对应一个最细粒度的能力子项与领域子项。
    """
    # 每条指令只针对一个具体的能力细分项和领域细分项
    cap_desc = cap_item
    dom_desc = dom_item
    diff_desc_list = difficulty.get(diff_key, [])
    diff_desc = diff_desc_list[0] if diff_desc_list else ""

    prompt = f"""
请你根据下面的信息，设计一条高质量的指令 / prompt，
用于后续指令微调数据构造（当前阶段只需要指令本身，不需要回答）。

- 能力类别: {cap_key}
- 能力细分示例: {cap_desc}
- 领域类别: {dom_key}
- 领域细分示例: {dom_desc}
- 难度等级: {diff_key}
- 难度说明: {diff_desc}

请你生成一条「用户提问 / 指令」（instruction/prompt），要求：
1. 仅构造用户侧指令，不需要任何回答内容
2. 内容尽量用中文，可以夹杂必要的英文术语
3. 真实、有用、具有代表性，能体现上述能力、领域和难度

请你**只输出一个 JSON 对象**，不要任何多余文字，字段包括：
- "instruction": 用户的指令 / prompt 文本
""".strip()

    return prompt


def _extract_json(text: str) -> str:
    """
    尝试从模型输出中提取 JSON 子串，尽量鲁棒一点。
    """
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        return text[start : end + 1]
    return text


def generate_sft_data(
    num_per_combination: int = 5,
    output_path: str = "instruction.jsonl",
    model_name: str = "DeepSeek-V3.2",
    mode: str = "online",
    sleep_seconds: float = 0.2,
    max_workers: int = 8,
) -> None:
    """
    遍历 capability x domain x difficulty，每种组合生成 num_per_combination 条「指令 / prompt」，
    只包含指令及元信息（后续再二次调用大模型生成 response），并写入 JSONL 文件。
    """
    system_content = (
        "你是一个高质量指令生成助手，负责根据给定的能力、领域和难度，"
        "生成用于指令微调的大模型指令（instruction/prompt）。务必严格按照用户要求输出 JSON，"
        "且只生成用户指令，不要生成回答。"
    )

    total_written = 0

    def _worker(
        cap_key: str,
        cap_item: str,
        dom_key: str,
        dom_item: str,
        diff_key: str,
        idx: int,
    ):
        user_content = build_user_prompt(
            cap_key,
            cap_item,
            dom_key,
            dom_item,
            diff_key,
        )

        try:
            content, reasoning_content = get_response(
                system_content=system_content,
                user_content=user_content,
                model_name=model_name,
                timeout=180,
                temperature=0.8,
                top_p=0.95,
                mode=mode,
            )
        except Exception as e:
            print(
                f"[ERROR] 调用大模型失败: cap={cap_key}, "
                f"dom={dom_key}, diff={diff_key}, idx={idx}, err={e}"
            )
            return None

        try:
            json_str = _extract_json(content)
            parsed = json.loads(json_str)
            if isinstance(parsed, dict):
                sample: Dict[str, Any] = parsed
            else:
                # 如果不是 JSON 对象，就直接当成指令字符串包一层
                sample = {"instruction": str(parsed)}
        except Exception as e:
            print(
                f"[WARN] 解析 JSON 失败，将原始内容作为 instruction 使用: "
                f"cap={cap_key}, dom={dom_key}, diff={diff_key}, idx={idx}, err={e}"
            )
            sample = {"instruction": content.strip()}

        # 补充 / 覆盖基础标签，保证元数据齐全
        # 将能力 / 领域写成「大类(子类)」的形式，方便后续分析
        sample.setdefault("capability", f"{cap_key}({cap_item})")
        sample.setdefault("domain", f"{dom_key}({dom_item})")
        sample.setdefault("difficulty", diff_key)

        if sleep_seconds > 0:
            time.sleep(sleep_seconds)

        return sample, cap_key, cap_item, dom_key, dom_item, diff_key

    with open(output_path, "w", encoding="utf-8") as fout:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []

            # 将多层 for 的每一次调用大模型的任务，提交到线程池并行执行
            for cap_key, cap_list in capability.items():
                for dom_key, dom_list in domain.items():
                    for cap_item in cap_list:
                        for dom_item in dom_list:
                            for diff_key in difficulty.keys():
                                for i in range(num_per_combination):
                                    futures.append(
                                        executor.submit(
                                            _worker,
                                            cap_key,
                                            cap_item,
                                            dom_key,
                                            dom_item,
                                            diff_key,
                                            i,
                                        )
                                    )

            for future in as_completed(futures):
                result = future.result()
                if result is None:
                    continue

                (
                    sample,
                    cap_key,
                    cap_item,
                    dom_key,
                    dom_item,
                    diff_key,
                ) = result

                fout.write(json.dumps(sample, ensure_ascii=False) + "\n")
                fout.flush()
                total_written += 1

                print(
                    f"[OK] 写入样本 #{total_written}: "
                    f"{cap_key}({cap_item}) | {dom_key}({dom_item}) | {diff_key}"
                )

    print(f"完成蒸馏，最终写入样本数量: {total_written}, 输出文件: {output_path}")


if __name__ == "__main__":
    # 默认：每种 (capability x domain x difficulty) 组合生成 5 条数据
    generate_sft_data()
