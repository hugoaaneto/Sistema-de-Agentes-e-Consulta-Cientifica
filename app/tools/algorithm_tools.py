from langchain.agents import Tool

from app.services.qa_service import (
    analyze_code,
    analyze_algorithm,
    answer_code_question,
)

algorithm_tools = [
    Tool(
        name="Code Analysis",
        func=analyze_code,
        description=(
            "Use this tool to analyze or explain code snippets based on a user's natural language question. "
            "The input should contain both the question and any contextual information, such as the expected behavior "
            "or execution details. Suitable for explaining logic, identifying bugs, or suggesting improvements."
        ),
    ),
    Tool(
        name="Algorithm Analysis",
        func=analyze_algorithm,
        description=(
            "Use this tool to analyze an algorithm based on a free-form question. "
            "This may include inquiries about its purpose, efficiency, complexity, or design choices. "
            "The input should provide the algorithm and any relevant context for a thorough analysis."
        ),
    ),
    Tool(
        name="General Code Question",
        func=answer_code_question,
        description=(
            "Use this tool to answer general programming or algorithm-related questions that do not require "
            "any additional context. Examples include: 'How do I implement quicksort?', "
            "'What is the difference between lists and tuples?', or 'What is recursion in Python?'."
        ),
    ),
]
