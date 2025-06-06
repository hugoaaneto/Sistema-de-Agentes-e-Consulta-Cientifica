from langchain.agents import Tool
from app.services.rag_pipeline import retrieve_relevant_passages

rag_tools = [
    Tool(
        name="RAG Retriever",
        func=retrieve_relevant_passages,
        description=(
            "Use this tool to retrieve relevant passages from documents in cloud storage. "
            "Input should be a string representing the user's question or query. "
            "The system will search the document base and return the most relevant information."
        ),
    ),
]
