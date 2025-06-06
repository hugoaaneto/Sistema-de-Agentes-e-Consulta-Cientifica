from langchain.agents import Tool

from app.services.cloud_storage import (
    delete_file,
    find_file,
    find_similar_files,
    get_all_storage_files,
    load_files_text,
)


cloud_storage_tools = [
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
        func=load_files_text,
        description=(
            "Use this tool to get the text of a file (or more) from the cloud bucket. "
            "Input should be a list of names of files in the bucket, such as ['document.pdf']."
        ),
    ),
    Tool(
        name="List All Files in GCS Bucket",
        func=lambda _: get_all_storage_files(),
        description=(
            "Use this tool to list all files currently stored in the cloud bucket. "
            "There is no specific input."
        ),
    ),
    Tool(
        name="Check if File Exists in GCS Bucket",
        func=find_file,
        description=(
            "Use this tool to check whether a specific file exists in the cloud bucket. "
            "Input should be the exact name of the file, such as 'document.pdf'."
        ),
    ),
    Tool(
        name="Find Similar File Names in GCS Bucket",
        func=find_similar_files,
        description=(
            "Use this tool to find files in the cloud bucket with names similar to the one provided. "
            "Input should be a single filename string, such as 'document_2023.pdf'. "
            "The tool will return a list of similar file names if any are found."
        ),
    ),
]
