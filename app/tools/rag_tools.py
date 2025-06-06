from langchain.agents import Tool

from app.services.cloud_storage import load_files_from_gcs


rag_tools = [
    Tool(
        name="Get relevant information from files",
        func=load_files_from_gcs,
        description=(
            "Use this tool to get the relevant information of a file (or more) from the cloud bucket. "
            "Input should be a list of names of files in the bucket, such as ['document.pdf']."
        ),
    ),
]
