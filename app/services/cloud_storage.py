import difflib
import os
import tempfile

from flask import current_app
from google.cloud import storage
from langchain.schema import Document

from app.services.text_processing import extract_text


def get_bucket():
    client = storage.Client()
    bucket_name = current_app.config["CLOUD_STORAGE_NAME"]
    return client.bucket(bucket_name)


def upload_file(file_storage_obj):
    try:
        bucket = get_bucket()
        blob = bucket.blob(file_storage_obj.filename)
        blob.upload_from_file(
            file_storage_obj.stream, content_type=file_storage_obj.content_type
        )
        return (
            f"Arquivo '{file_storage_obj.filename}' enviado com sucesso para o bucket."
        )
    except Exception as e:
        return f"Erro ao enviar arquivo: {e}"


def get_all_storage_files():
    try:
        bucket = get_bucket()
        blobs = bucket.list_blobs()
        # Para uma prova de conceito utilizei apenas PDFs
        return [blob.name for blob in blobs if blob.name.endswith((".pdf"))]
    except Exception as e:
        return f"Erro ao carregar a listagem dos arquivo: {e}"


def download_file(filename, destination_path):
    try:
        bucket = get_bucket()
        blob = bucket.blob(filename)
        blob.download_to_filename(destination_path)
    except Exception as e:
        return f"Erro ao baixar o arquivo {filename}: {e}"


def delete_file(file_name: str):
    try:
        bucket = get_bucket()
        blob = bucket.blob(file_name)

        # Caso não encontre um arquivo com o nome indicado
        if not blob.exists():
            return f"Arquivo '{file_name}' não encontrado no bucket."

        blob.delete()
        return f"Arquivo '{file_name}' removido com sucesso do bucket."
    except Exception as e:
        return f"Erro ao deletar o arquivo '{file_name}': {e}"


def load_files_text(filenames: list[str] = None):
    available_files = get_all_storage_files()
    target_files = (
        [f for f in available_files if f in filenames] if filenames else available_files
    )

    texts = []
    for file_name in target_files:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_path = tmp.name
        try:
            download_file(file_name, tmp_path)
            text = extract_text(tmp_path)
            if text:
                texts.append(text)
        finally:
            os.remove(tmp_path)

    return texts


def load_files_documents():
    available_files = get_all_storage_files()

    documents = []
    for file_name in available_files:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_path = tmp.name
        try:
            download_file(file_name, tmp_path)
            text = extract_text(tmp_path)
            if text:
                doc = Document(page_content=text, metadata={"filename": file_name})
                documents.append(doc)
        finally:
            os.remove(tmp_path)

    return documents


def find_file(filename: str):
    all_files = get_all_storage_files()

    if filename in all_files:
        return f"O arquivo '{filename}' já está armazenado no CloudStorate."

    return f"O arquivo '{filename}' não foi localizado."


def find_similar_files(filename: str):
    all_files = get_all_storage_files()

    similar = difflib.get_close_matches(filename, all_files, n=4, cutoff=0.8)

    if similar:
        return "Arquivo similar identificado:\n\n".join(f"- {name}" for name in similar)

    return f"O arquivo '{filename}' não foi localizado nem arquivos semelhantes."
