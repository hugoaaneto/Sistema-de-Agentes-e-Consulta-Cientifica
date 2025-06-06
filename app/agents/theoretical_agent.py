from app.agents.agent_factory import create_agent
from app.tools.theoretical_tools import theoretical_tools

"""
Agente de responder duvidas teoricas:

Responsável pela extração de informações relevantes de artigos cientificos a partir de uma query
"""


def initialize_theoretical_agent(query: str):
    agent = create_agent(theoretical_tools)
    return agent.invoke({"input": query})
