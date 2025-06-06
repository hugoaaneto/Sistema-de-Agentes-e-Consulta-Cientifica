from langchain.agents import initialize_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from flask import current_app

from app.tools.orchestrator_tools import orchestrator_tools


def create_agent():
    gemini_llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-lite",
        temperature=0.3,
        google_api_key=current_app.config["GEMINI_API_KEY"],
    )

    agent = initialize_agent(
        tools=orchestrator_tools,
        llm=gemini_llm,
        agent="zero-shot-react-description",
        verbose=True,
    )
    return agent


def orchestrate_flow(message: str):
    agent = create_agent()
    response = agent.run(message)
    return response
