from app.agents.agent_factory import create_agent
from app.tools.rag_tools import rag_tools

"""
Agente de Retrieval-Augmented Generation (RAG):

Responsável pela extração de informações relevantes de artigos cientificos a partir de uma query
"""


def initialize_rag_agent(query: str):
    agent = create_agent(rag_tools)
    return agent.invoke({"input": query})
