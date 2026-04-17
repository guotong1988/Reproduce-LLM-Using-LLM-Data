# capability x domain x difficulty x nlp_task

capability = {}

capability["通用对话"] = [
    # 原始子项
    "闲聊",
    "情感陪伴",
    "角色扮演",
    "日常问候",
    "观点讨论",
    "冲突化解",
    "建议与决策陪伴",
    # 扩展子项
    "闲聊与日常寒暄",
    "情感陪伴与安慰",
    "角色扮演与代入式对话",
    "日常问候与寒暄续聊",
    "观点讨论与价值观碰撞",
    "冲突化解与矛盾调停",
    "跨文化交流与礼仪注意",
    "表达润色与话术优化",
    "压力疏导与情绪共情（非专业心理咨询）",
    "多轮追问与上下文承接",
    "人际沟通话术设计",
]
capability["知识问答"] = [
    # 原始子项
    "事实性查询",
    "百科知识",
    "概念解释",
    "定义辨析",
    "历史事件问答",
    "数据与统计解读",
    "背景信息补充",
    # 扩展子项
    "事实性查询与精确回答",
    "百科知识检索与整合",
    "概念解释与通俗类比",
    "定义辨析与相近概念区分",
    "历史事件问答与时间线梳理",
    "数据与统计解读与风险提示",
    "背景信息补充与延伸阅读建议",
    "术语解释与专业词汇通俗化",
    "多来源信息对比与一致性判断",
    "模糊问题澄清与范围界定",
    "常见误区澄清与谣言辨析",
    "考试风格题目知识点讲解",
]
capability["内容创作"] = [
    # 原始子项
    "写作",
    "邮件",
    "文案",
    "诗歌",
    "剧本",
    "报告撰写",
    "演讲稿",
    "社交媒体内容",
    "课程大纲与教学设计",
    # 扩展子项
    "议论文写作与观点展开",
    "说明文与科普文章写作",
    "邮件与商务沟通写作",
    "文案与宣传语创作",
    "诗歌与歌词创作",
    "剧本与分镜大纲构思",
    "报告撰写与结构设计",
    "演讲稿与发言稿撰写",
    "社交媒体内容与话题运营文案",
    "课程大纲与教学设计",
    "学习笔记与知识卡片生成",
    "多版本改写与风格迁移",
    "多语言内容互译与本地化润色",
]
capability["逻辑推理"] = [
    # 原始子项
    "数学",
    "科学推理",
    "常识推理",
    "归纳推理",
    "演绎推理",
    "反事实推理",
    "题目步骤拆解",
    "谜题与逻辑游戏",
    # 扩展子项
    "数学题解与步骤推导",
    "科学推理与因果分析",
    "常识推理与场景合理性判断",
    "归纳推理与模式发现",
    "演绎推理与形式逻辑",
    "反事实推理与假设分析",
    "题目步骤拆解与中间结果展示",
    "谜题与逻辑游戏求解",
    "选项排除与最优解选择",
    "错误定位与推理链自检",
    "多条件约束下的方案比较",
    "不确定条件下的决策推理",
]
capability["代码技术"] = [
    # 原始子项
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
    # 扩展子项
    "代码编写与实现思路设计",
    "调试与错误信息分析",
    "代码解释与重构意图说明",
    "SQL 查询与数据库操作设计",
    "Shell 脚本与命令行自动化",
    "代码优化与性能分析建议",
    "重构与可读性、可维护性提升",
    "单元测试编写与用例设计",
    "API 设计与接口文档草拟",
    "代码审查与改进建议",
    "多语言示例代码对照",
    "简单架构设计与模块划分",
]
capability["长文本处理"] = [
    # 原始子项
    "摘要",
    "提取",
    "长文档问答",
    "结构化重写",
    "关键信息对比",
    "多文档信息汇总",
    "思维导图与提纲生成",
    # 扩展子项
    "篇章级摘要与关键信息压缩",
    "要点提取与条目化整理",
    "长文档问答与定位证据片段",
    "结构化重写与逻辑重组",
    "关键信息对比与差异分析",
    "多文档信息汇总与统一口径输出",
    "思维导图与提纲生成",
    "长对话记录梳理与会议纪要生成",
    "合同、协议等条款拆解与要点列举（不构成法律意见）",
    "读书笔记与章节脉络梳理",
    "论文段落改写与语言润色（不代写）",
]
capability["多模态/工具"] = [
    # 原始子项
    "调用API",
    "画图指令",
    "表格处理",
    "文件解析",
    "浏览器或搜索工具调用",
    "日程与待办管理工具",
    # 扩展子项
    "调用API与参数构造示例",
    "画图指令与可视化草图描述",
    "表格处理与字段设计建议",
    "文件解析与结构化抽取思路",
    "浏览器或搜索工具调用提示词设计",
    "日程与待办管理工具使用建议",
    "代码执行类工具的输入输出设计",
    "数据分析工具（如表格/BI）的分析思路",
    "RAG/检索增强场景中的查询构造",
    "多模态对话中图文结合的指令设计",
]

domain = {}
domain["基础学科"] = [
    "文学",
    "历史",
    "哲学",
    "数学",
    "物理",
    "化学",
    "生物",
    "地理",
    "计算机基础",
    "逻辑学",
    "统计学",
    "语言学",
]
domain["垂直专业"] = [
    "医疗",
    "法律",
    "金融",
    "教育",
    "心理学",
    "新闻传媒",
    "管理学",
    "市场营销",
    "人力资源",
    "会计与审计",
]
domain["生活服务"] = [
    "旅游",
    "餐饮",
    "购物",
    "家政",
    "交通出行",
    "健康养生",
    "亲子育儿",
    "宠物照护",
    "居家收纳与整理",
    "个人成长与时间管理",
]
domain["工程技术"] = [
    "机械",
    "建筑",
    "电子",
    "化工",
    "土木",
    "自动化",
    "材料",
    "航空航天",
    "海洋工程",
    "能源与环保",
    "工业设计",
]
domain["互联网/IT"] = [
    "产品",
    "运营",
    "开发",
    "数据",
    "安全",
    "测试",
    "运维",
    "人工智能与大模型",
    "区块链与加密应用",
    "增长与用户增长策略",
]
domain["政务/公文"] = [
    "政策解读",
    "公文写作",
    "政府服务",
    "会议纪要",
    "通知公告",
    "工作总结与述职材料",
    "规划方案与实施细则",
]

difficulty = {}
difficulty["Level-1"] = ["简单指令，单轮对话"]
difficulty["Level-2"] = ["复杂指令，需要多步推理"]
difficulty["Level-3"] = ["专家级任务"]

# NLP 任务类型：约束指令形态（问答/摘要/翻译等）
nlp_task = {}
nlp_task["问答"] = ["用户提出问题，模型给出直接回答；可含多轮澄清"]
nlp_task["摘要"] = ["对给定文本或对话进行压缩、提炼要点与结构"]
nlp_task["翻译"] = ["跨语言互译或语域/风格对齐的译写"]
nlp_task["改写"] = ["同义改写、风格迁移、扩写缩写、语气调整等"]
nlp_task["分类"] = ["打标签、主题/意图分类、多标签或层次分类"]
nlp_task["信息抽取"] = ["实体、关系、事件、表格字段等结构化抽取"]
nlp_task["推理"] = ["链式推理、约束求解、比较与论证"]
nlp_task["代码"] = ["编写、解释、调试、重构、测试或接口设计等代码相关任务"]
nlp_task["工具调用格式"] = ["函数/工具 JSON、API 参数、命令行或检索查询等可执行调用形态"]
nlp_task["安全拒答"] = ["不当/越界请求下礼貌拒绝、边界说明与合规引导"]

import json
from typing import Dict, Any


def build_user_prompt(
    cap_key: str,
    cap_item: str,
    dom_key: str,
    dom_item: str,
    diff_key: str,
    nlp_key: str,
) -> str:
    """
    根据能力 / 领域 / 难度 / NLP 任务类型构造给大模型的提示词，
    让大模型只返回一条「用户指令 / prompt」的 JSON。
    其中每条指令只对应一个最细粒度的能力子项与领域子项。
    """
    # 每条指令只针对一个具体的能力细分项和领域细分项
    cap_desc = cap_item
    dom_desc = dom_item
    diff_desc_list = difficulty.get(diff_key, [])
    diff_desc = diff_desc_list[0] if diff_desc_list else ""
    nlp_desc_list = nlp_task.get(nlp_key, [])
    nlp_desc = nlp_desc_list[0] if nlp_desc_list else ""

    prompt = f"""
请你根据下面的信息，设计一条高质量的指令 / prompt，
用于后续指令微调数据构造（当前阶段只需要指令本身，不需要回答）。

- 能力类别: {cap_key}
- 能力细分示例: {cap_desc}
- 领域类别: {dom_key}
- 领域细分示例: {dom_desc}
- 难度等级: {diff_key}
- 难度说明: {diff_desc}
- NLP 任务类型: {nlp_key}
- NLP 任务说明: {nlp_desc}

请你生成一条「用户提问 / 指令」（instruction/prompt），要求：
1. 仅构造用户侧指令，不需要任何回答内容
2. 内容尽量用中文，可以夹杂必要的英文术语
3. 真实、有用、具有代表性，能体现上述能力、领域、难度与 NLP 任务形态（指令应符合所选 NLP 任务类型）

请你只输出一个 用户的指令 / prompt 文本，不要任何多余文字
""".strip()

    return prompt


def generate_data(
    num_per_combination: int = 2,
    output_path: str = "distill_instruction_prompt_cn.jsonl",
) -> None:
    """
    遍历 capability x domain x difficulty x nlp_task，把每次要传给任意大模型推理接口
    的输入参数写入 JSONL（每行一个请求对象），供后续批量推理使用。
    """
    system_content = (
        "你是一个高质量指令生成助手，负责根据给定的能力、领域、难度与 NLP 任务类型，"
        "生成用于指令微调的大模型指令（instruction/prompt）。务必严格按照用户要求输出 JSON，"
        "且只生成用户指令，不要生成回答。"
    )

    total_written = 0

    with open(output_path, "w", encoding="utf-8") as fout:
        for cap_key, cap_list in capability.items():
            for dom_key, dom_list in domain.items():
                for cap_item in cap_list:
                    for dom_item in dom_list:
                        for diff_key in difficulty.keys():
                            for nlp_key in nlp_task.keys():
                                for i in range(num_per_combination):
                                    user_content = build_user_prompt(
                                        cap_key,
                                        cap_item,
                                        dom_key,
                                        dom_item,
                                        diff_key,
                                        nlp_key,
                                    )
                                    record: Dict[str, Any] = {
                                        # 下游可直接用这几个字段调用任意大模型推理接口
                                        "system_content": system_content,
                                        "user_content": user_content,
                                        # 保留标签，便于后续追踪与分析
                                        "capability": f"{cap_key}({cap_item})",
                                        "domain": f"{dom_key}({dom_item})",
                                        "difficulty": diff_key,
                                        "nlp_task": nlp_key,
                                    }

                                    fout.write(json.dumps(record, ensure_ascii=False) + "\n")
                                    total_written += 1

                                    print(
                                        f"[OK] 写入请求 #{total_written}: "
                                        f"{cap_key}({cap_item}) | {dom_key}({dom_item}) | {diff_key} | {nlp_key} | idx={i}"
                                    )

    print(f"完成生成，最终写入请求数量: {total_written}, 输出文件: {output_path}")


if __name__ == "__main__":
    # 默认：每种 (capability x domain x difficulty x nlp_task) 组合生成 5 条数据
    generate_data()
