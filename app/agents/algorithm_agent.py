from app.agents.agent_factory import create_agent
from app.tools.algorithm_tools import algorithm_tools

"""
Agente de responder duvidas algoritimicas ou de codigo:

Responsável pela extração de informações relevantes de artigos cientificos a partir de uma query
"""


def initialize_algorithm_agent(query: str):
    agent = create_agent(algorithm_tools)
    return agent.invoke({"input": query})
