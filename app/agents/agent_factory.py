from flask import current_app, g
from langchain.agents import initialize_agent
from langchain_community.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI


def get_llm(llm_name="gemini"):
    if llm_name == "gemini":
        return ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-lite",
            temperature=0.3,
            google_api_key=current_app.config["GEMINI_API_KEY"],
        )
    elif llm_name == "openai":
        return ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.3,
            openai_api_key=current_app.config["OPENAI_API_KEY"],
        )
    else:
        raise ValueError(f"LLM não disponivel: {llm_name}")


def create_agent(tools, llm_name="gemini"):
    if hasattr(g, "llm_name"):
        llm_name = g.llm_name
    llm = get_llm(llm_name)

    return initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True,
    )
