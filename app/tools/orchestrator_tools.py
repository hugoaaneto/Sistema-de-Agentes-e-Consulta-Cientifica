from langchain.agents import Tool

from app.agents.rag_agent import initialize_rag_agent
from app.agents.algorithm_agent import initialize_algorithm_agent
from app.agents.theoretical_agent import initialize_theoretical_agent
from app.agents.cloud_storage_agent import initialize_cloud_storage_agent
from app.services.llm_api import set_current_llm


orchestrator_tools = [
    # Para testes
    Tool(
        name="Hello",
        func=lambda _: "Olá! Como posso ajuda-lo?",
        description=(
            "Use this tool when the user greets the agent, says hello, or starts the conversation casually. "
            "The input may be something like 'hi', 'hello', or 'hey'."
        ),
    ),
    Tool(
        name="Switch LLM Model",
        func=set_current_llm,
        description=(
            "Use this tool to change the underlying LLM being used (e.g., from GPT to Gemini). "
            "If the user mentioned google use 'gemini' and if the user mentions GPT use 'openai'."
            "The input should be the name of the desired model, being 'gemini' or 'openai'."
        ),
    ),
    Tool(
        name="RAG Document Search",
        func=initialize_rag_agent,
        description=(
            "Use this tool when the user asks a scientific or technical question. "
            "The system will search for relevant information in the available knowledge base using Retrieval-Augmented Generation (RAG) "
            "and generate a response based on the retrieved content. "
            "Input must be a string that is used as a query for the RAG search."
        ),
    ),
    Tool(
        name="Cloud Storage Agent",
        func=initialize_cloud_storage_agent,
        description=(
            "Use this tool when the user asks to read, delete, or manage files stored in the cloud storage bucket. "
            "Examples: 'delete document.pdf', 'read file.txt', or 'list all documents'. "
            "Input must describe the action to be performed on the storage."
        ),
    ),
    Tool(
        name="Algorithm Agent",
        func=initialize_algorithm_agent,
        description=(
            "Use this tool when the user asks about programming algorithms, coding issues, or implementation help. "
            "Examples: 'how to implement quicksort?', 'why is my for loop slow?', 'how to optimize this code?'."
        ),
    ),
    Tool(
        name="Theoretical Agent",
        func=initialize_theoretical_agent,
        description=(
            "Use this tool when the user asks about theoretical concepts in computer science, AI, or mathematics. "
            "Examples: 'what is overfitting?', 'explain reinforcement learning', or 'difference between CNN and RNN'."
        ),
    ),
]
