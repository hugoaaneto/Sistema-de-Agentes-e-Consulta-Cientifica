from flask import current_app
from langchain.agents import initialize_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from app.tools.rag_tools import rag_tools


def create_rag_agent():
    gemini_llm = ChatGoogleGenerativeAI(
        model="gemini-2.0",
        temperature=0.3,
        google_api_key=current_app.config["GEMINI_API_KEY"],
    )

    agent = initialize_agent(
        tools=rag_tools,
        llm=gemini_llm,
        agent="zero-shot-react-description",
        verbose=True,
    )
    return agent


def handle_rag_query(query: str, filenames: list[str] = None):
    agent = create_rag_agent()
    return agent.run({"query": query, "filenames": filenames})
