from app.services.llm_api import generate_response


def answer_specific_question(input: str):
    prompt = f"A partir exclusivamente das informações providas abaixo responda em portugues a pergunta: \n{input}"
    return generate_response(prompt)


def answer_general_question(question: str):
    prompt = f"Responda de forma precisa e clara a seguinte pergunta em portugues:\n{question}"
    return generate_response(prompt)


def analyze_code(input: str):
    prompt = f"""Analise tecnicamente o código ou a questão de programação descrita a seguir, 
    considerando apenas as informações fornecidas. Forneça a resposta em português de forma clara,
    apontando comportamento, erros, limitações ou sugestões de melhoria, se aplicável: \n{input}"""

    return generate_response(prompt)


def analyze_algorithm(input: str):
    prompt = f"""A seguir está uma solicitação sobre um algoritmo. Analise e responda com clareza
    em português,considerando o contexto fornecido. Inclua aspectos como funcionamento, complexidade
    e aplicação, se relevante: \n{input}"""

    return generate_response(prompt)


def answer_code_question(input: str):
    prompt = f"""Responda à seguinte pergunta sobre programação ou algoritmos de forma direta,
    precisa e em português. A pergunta não exige informações adicionais: \n {input}"""

    return generate_response(prompt)
