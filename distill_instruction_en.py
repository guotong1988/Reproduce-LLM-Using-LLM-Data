# capability x domain x difficulty x nlp_task

capability = {}

capability["General Conversation"] = [
    # Original items
    "Casual chat",
    "Emotional support",
    "Role play",
    "Daily greetings",
    "Opinion discussion",
    "Conflict resolution",
    "Advice and decision support",
    # Expanded items
    "Casual chat and daily small talk",
    "Emotional support and comfort",
    "Role play and immersive dialogue",
    "Daily greetings and follow-up conversation",
    "Opinion discussion and value-based debate",
    "Conflict resolution and mediation",
    "Cross-cultural communication and etiquette awareness",
    "Expression polishing and phrasing optimization",
    "Stress relief and emotional empathy (non-clinical mental support)",
    "Multi-turn follow-up and context carryover",
    "Interpersonal communication script design",
]
capability["Knowledge QA"] = [
    # Original items
    "Factual lookup",
    "Encyclopedic knowledge",
    "Concept explanation",
    "Definition disambiguation",
    "Historical event QA",
    "Data and statistics interpretation",
    "Background context enrichment",
    # Expanded items
    "Factual lookup with precise answers",
    "Encyclopedic retrieval and synthesis",
    "Concept explanation with plain-language analogies",
    "Definition disambiguation and similar-concept differentiation",
    "Historical event QA with timeline structuring",
    "Data/statistics interpretation with risk caveats",
    "Background context enrichment with further-reading suggestions",
    "Terminology explanation and jargon simplification",
    "Multi-source comparison and consistency checking",
    "Ambiguous question clarification and scope definition",
    "Common misconception correction and misinformation analysis",
    "Exam-style knowledge point explanation",
]
capability["Content Creation"] = [
    # Original items
    "Writing",
    "Email",
    "Copywriting",
    "Poetry",
    "Scriptwriting",
    "Report drafting",
    "Speech writing",
    "Social media content",
    "Course outline and instructional design",
    # Expanded items
    "Argumentative writing and claim development",
    "Expository and popular science writing",
    "Email and business communication writing",
    "Copywriting and slogan creation",
    "Poetry and lyric writing",
    "Scriptwriting and storyboard outline ideation",
    "Report drafting and structure design",
    "Speech and presentation script writing",
    "Social media content and topic campaign copy",
    "Course outline and instructional design",
    "Study notes and knowledge card generation",
    "Multi-version rewriting and style transfer",
    "Multilingual translation and localization polishing",
]
capability["Logical Reasoning"] = [
    # Original items
    "Mathematics",
    "Scientific reasoning",
    "Common-sense reasoning",
    "Inductive reasoning",
    "Deductive reasoning",
    "Counterfactual reasoning",
    "Step-by-step problem decomposition",
    "Puzzles and logic games",
    # Expanded items
    "Math problem solving with step derivations",
    "Scientific reasoning and causal analysis",
    "Common-sense reasoning and scenario plausibility judgment",
    "Inductive reasoning and pattern discovery",
    "Deductive reasoning and formal logic",
    "Counterfactual reasoning and hypothesis analysis",
    "Step-by-step decomposition with intermediate results",
    "Puzzle and logic game solving",
    "Option elimination and optimal solution selection",
    "Error localization and reasoning-chain self-check",
    "Plan comparison under multi-constraint settings",
    "Decision reasoning under uncertainty",
]
capability["Coding & Technology"] = [
    # Original items
    "Implementation",
    "Debugging",
    "Explanation",
    "SQL",
    "Shell",
    "Code optimization",
    "Refactoring",
    "Unit test writing",
    "API design",
    "Code review and suggestions",
    # Expanded items
    "Code implementation and solution design",
    "Debugging and error-message analysis",
    "Code explanation and refactoring rationale",
    "SQL query and database operation design",
    "Shell scripting and command-line automation",
    "Code optimization and performance analysis suggestions",
    "Refactoring for readability and maintainability",
    "Unit test writing and test case design",
    "API design and interface documentation drafting",
    "Code review and improvement suggestions",
    "Cross-language example code comparison",
    "Lightweight architecture and module decomposition",
]
capability["Long-Context Processing"] = [
    # Original items
    "Summarization",
    "Extraction",
    "Long-document QA",
    "Structured rewriting",
    "Key information comparison",
    "Multi-document synthesis",
    "Mind map and outline generation",
    # Expanded items
    "Document-level summarization and key-information compression",
    "Key-point extraction and bullet-style organization",
    "Long-document QA with evidence localization",
    "Structured rewriting and logical reorganization",
    "Key-information comparison and difference analysis",
    "Multi-document synthesis with unified output style",
    "Mind map and outline generation",
    "Long conversation consolidation and meeting-minute generation",
    "Clause decomposition for contracts/agreements (not legal advice)",
    "Book note generation and chapter-structure mapping",
    "Academic paragraph rewriting and language polishing (no ghostwriting)",
]
capability["Multimodal/Tools"] = [
    # Original items
    "API calling",
    "Drawing instructions",
    "Spreadsheet processing",
    "File parsing",
    "Browser/search tool usage",
    "Schedule and todo tools",
    # Expanded items
    "API calling with parameter construction examples",
    "Drawing instructions and visual sketch descriptions",
    "Spreadsheet processing and field design suggestions",
    "File parsing and structured extraction strategy",
    "Prompt design for browser/search tool usage",
    "Usage recommendations for scheduling and todo tools",
    "Input/output design for code-execution tools",
    "Analysis approaches for data tools (e.g., spreadsheet/BI)",
    "Query construction in RAG/retrieval-augmented scenarios",
    "Instruction design for image-text multimodal dialogue",
]

domain = {}
domain["Fundamental Disciplines"] = [
    "Literature",
    "History",
    "Philosophy",
    "Mathematics",
    "Physics",
    "Chemistry",
    "Biology",
    "Geography",
    "Computer fundamentals",
    "Logic",
    "Statistics",
    "Linguistics",
]
domain["Vertical Professions"] = [
    "Healthcare",
    "Law",
    "Finance",
    "Education",
    "Psychology",
    "Journalism and media",
    "Management",
    "Marketing",
    "Human resources",
    "Accounting and auditing",
]
domain["Daily Life Services"] = [
    "Travel",
    "Food and dining",
    "Shopping",
    "Household services",
    "Transportation and commuting",
    "Health and wellness",
    "Parenting",
    "Pet care",
    "Home organization and decluttering",
    "Personal growth and time management",
]
domain["Engineering & Technology"] = [
    "Mechanical engineering",
    "Architecture",
    "Electronics",
    "Chemical engineering",
    "Civil engineering",
    "Automation",
    "Materials science",
    "Aerospace",
    "Marine engineering",
    "Energy and environmental protection",
    "Industrial design",
]
domain["Internet/IT"] = [
    "Product management",
    "Operations",
    "Software development",
    "Data",
    "Security",
    "Testing/QA",
    "DevOps/SRE",
    "AI and large language models",
    "Blockchain and cryptographic applications",
    "Growth and user acquisition strategy",
]
domain["Government & Official Writing"] = [
    "Policy interpretation",
    "Official document drafting",
    "Public service guidance",
    "Meeting minutes",
    "Notices and announcements",
    "Work summary and performance reports",
    "Planning proposals and implementation guidelines",
]

difficulty = {}
difficulty["Level-1"] = ["Simple instruction, single-turn dialogue"]
difficulty["Level-2"] = ["Complex instruction, requires multi-step reasoning"]
difficulty["Level-3"] = ["Expert-level task"]

# NLP task types: constrain instruction format (QA/summarization/translation/etc.)
nlp_task = {}
nlp_task["Question Answering"] = [
    "User asks a question and the model provides a direct answer; may include multi-turn clarification"
]
nlp_task["Summarization"] = [
    "Compress and extract key points/structure from given text or dialogue"
]
nlp_task["Translation"] = [
    "Cross-lingual translation or register/style-aligned rewriting"
]
nlp_task["Rewriting"] = [
    "Paraphrasing, style transfer, expansion/condensation, tone adjustment, etc."
]
nlp_task["Classification"] = [
    "Labeling, topic/intent classification, multi-label or hierarchical classification"
]
nlp_task["Information Extraction"] = [
    "Structured extraction of entities, relations, events, table fields, etc."
]
nlp_task["Reasoning"] = [
    "Chain-of-thought style reasoning, constrained solving, comparison, and argumentation"
]
nlp_task["Coding"] = [
    "Code-related tasks such as writing, explanation, debugging, refactoring, testing, or API design"
]
nlp_task["Tool Calling Format"] = [
    "Executable call formats such as function/tool JSON, API parameters, CLI commands, or retrieval queries"
]
nlp_task["Safe Refusal"] = [
    "Polite refusal, boundary explanation, and compliant guidance for inappropriate/out-of-scope requests"
]

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
    Build an instruction-generation prompt from capability/domain/difficulty/NLP task type.
    The model must return only one JSON object containing a user instruction/prompt.
    Each instruction should correspond to exactly one fine-grained capability item and one domain item.
    """
    # Each instruction targets one concrete capability sub-item and one domain sub-item.
    cap_desc = cap_item
    dom_desc = dom_item
    diff_desc_list = difficulty.get(diff_key, [])
    diff_desc = diff_desc_list[0] if diff_desc_list else ""
    nlp_desc_list = nlp_task.get(nlp_key, [])
    nlp_desc = nlp_desc_list[0] if nlp_desc_list else ""

    prompt = f"""
Please design one high-quality instruction/prompt based on the information below.
This instruction will be used for instruction-tuning data construction (at this stage, only the instruction itself is needed, not the answer).

- Capability Category: {cap_key}
- Capability Sub-item Example: {cap_desc}
- Domain Category: {dom_key}
- Domain Sub-item Example: {dom_desc}
- Difficulty Level: {diff_key}
- Difficulty Description: {diff_desc}
- NLP Task Type: {nlp_key}
- NLP Task Description: {nlp_desc}

Generate exactly one user question/instruction (instruction/prompt) with these requirements:
1. Construct only the user-side instruction; do not include any answer content
2. Write the instruction in English
3. Keep it realistic, useful, and representative of the selected capability, domain, difficulty, and NLP task format (the instruction should match the selected NLP task type)

Output only one JSON object with no extra text. The object must contain:
- "instruction": the user's instruction/prompt text
""".strip()

    return prompt


def generate_data(
    num_per_combination: int = 2,
    output_path: str = "deepseek_prompts_en.jsonl",
) -> None:
    """
    Iterate over capability x domain x difficulty x nlp_task and write input parameters
    for deepseek_infer.get_response into JSONL (one request object per line),
    for downstream batch inference.
    """
    system_content = (
        "You are a high-quality instruction generation assistant. "
        "Given capability, domain, difficulty, and NLP task type, generate an instruction "
        "(instruction/prompt) for instruction tuning. Strictly output JSON as requested, "
        "and generate only the user instruction, not the answer."
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
                                        # These fields can be used directly by deepseek_infer.get_response downstream.
                                        "system_content": system_content,
                                        "user_content": user_content,
                                        # Keep tags for tracking and analysis.
                                        "capability": f"{cap_key}({cap_item})",
                                        "domain": f"{dom_key}({dom_item})",
                                        "difficulty": diff_key,
                                        "nlp_task": nlp_key,
                                    }

                                    fout.write(json.dumps(record, ensure_ascii=False) + "\n")
                                    total_written += 1

                                    print(
                                        f"[OK] Request #{total_written} written: "
                                        f"{cap_key}({cap_item}) | {dom_key}({dom_item}) | {diff_key} | {nlp_key} | idx={i}"
                                    )

    print(f"Generation completed. Total requests written: {total_written}, output file: {output_path}")


if __name__ == "__main__":
    # Default: generate 5 samples per (capability x domain x difficulty x nlp_task) combination.
    generate_data()
