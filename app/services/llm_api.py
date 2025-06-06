import google.generativeai as genai
import openai
from flask import current_app, g


def set_current_llm(llm_name: str):
    valid_llms = ["gemini", "openai"]
    if llm_name in valid_llms:
        g.llm_name = llm_name
        return f"Troca realizada com sucesso, LLM atual é {llm_name}!"
    else:
        return "LLM invalida, as opções aceitas são 'gemini' ou 'openai'"


def generate_response(prompt):
    if hasattr(g, "llm_name"):
        if g.llm_name == "gemini":
            return generate_gemini(prompt)
        elif g.llm_name == "openai":
            return generate_openai(prompt)

    # Default model
    return generate_gemini(prompt)


def generate_openai(prompt):
    openai.api_key = current_app.config["OPENAI_API_KEY"]

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1600,
        temperature=0.3,
    )

    return response.choices[0].message.content


def generate_gemini(prompt):
    genai.configure(api_key=current_app.config["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-2.0-flash-lite")

    generation_config = genai.types.GenerationConfig(
        max_output_tokens=1600, temperature=0.3
    )

    response = model.generate_content(prompt, generation_config=generation_config)

    return response.text
