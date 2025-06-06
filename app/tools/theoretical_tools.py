from langchain.agents import Tool

from app.services.qa_service import answer_general_question, answer_specific_question

theoretical_tools = [
    Tool(
        name="Specific Question",
        func=answer_specific_question,
        description=(
            "Use this tool to answer specific questions based strictly on a provided article excerpt. "
            "The input must be a string with the question and the necessary information to answer it."
        ),
    ),
    Tool(
        name="General Question",
        func=answer_general_question,
        description=(
            "Use this tool to handle general theoretical or conceptual questions. "
            "The answer is generated based on the LLM’s general knowledge."
            "The input is a question of well know general information."
        ),
    ),
]
