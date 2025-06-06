from app.agents.agent_factory import create_agent
from app.tools.orchestrator_tools import orchestrator_tools

"""
Agente de orquestração:

Responsável pelo primeiro contato com o usuário, faz uma identificação inicial do objetivo do usuário naquela conversa
Realiza a função de roteador inteligente, direcionando a um agente especializado de acordo com a solicitação do usuario
Capaz de trocar modelo de LLM, iniciar a conversa e ativar outros agentes
"""


def initialize_orchestrate_agent(message: str):
    agent = create_agent(orchestrator_tools)
    return agent.invoke(message)
