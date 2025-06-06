from app.agents.agent_factory import create_agent
from app.tools.cloud_storage_tools import cloud_storage_tools

"""
Agente para lidar com o armazenamento de artigos:

Responsável por fazer leituras, deleções, trazer textos etc.
"""


def initialize_cloud_storage_agent(message: str):
    agent = create_agent(cloud_storage_tools)
    return agent.invoke(message)
