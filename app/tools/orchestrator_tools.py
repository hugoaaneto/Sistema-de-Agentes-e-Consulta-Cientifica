from langchain.agents import Tool

from app.services.cloud_storage import delete_file, load_files_from_gcs


orchestrator_tools = [
    # Para testes
    Tool(
        name="Hello!",
        func=lambda x: "Hello! How can I assist you today?",
        description=(
            "Use this tool when the user greets the agent, says hello, or starts the conversation casually. "
            "The input may be something like 'hi', 'hello', or 'hey'."
        ),
    ),
    Tool(
        name="Delete File from GCS Bucket",
        func=delete_file,
        description=(
            "Use this tool to delete a file from the cloud bucket. "
            "Input should be the name of the file in the bucket, such as 'document.pdf'."
        ),
    ),
    Tool(
        name="Get File text from GCS Bucket",
        func=load_files_from_gcs,
        description=(
            "Use this tool to get the text of a file (or more) from the cloud bucket. "
            "Input should be a list of names of files in the bucket, such as ['document.pdf']."
        ),
    ),
    Tool(
        name="Switch LLM Model",
        func=lambda x: "Modelo trocado com sucesso",
        description=(
            "Use this tool to change the underlying LLM being used (e.g., from GPT-4 to Gemini). "
            "The input should be the name of the desired model, such as 'gemini' or 'gpt-4'."
        ),
    ),
    Tool(
        name="Answer Question with RAG",
        func=lambda x: "resposta indisponivel no momento, tente novamente mais tarde",
        description=(
            "Use this tool to answer a user's question using Retrieval-Augmented Generation. "
            "The input should be a natural language question that can be answered from the documents."
        ),
    ),
]
