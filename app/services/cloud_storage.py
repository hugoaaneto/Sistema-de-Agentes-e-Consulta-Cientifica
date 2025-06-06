import os
import tempfile

from flask import current_app
from google.cloud import storage

from app.services.text_processing import extract_text


def upload_file(file_storage_obj):
    storage_client = storage.Client()
    BUCKET_NAME = current_app.config["CLOUD_STORAGE_NAME"]

    try:
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(file_storage_obj.filename)
        blob.upload_from_file(
            file_storage_obj.stream, content_type=file_storage_obj.content_type
        )
        return (
            f"Arquivo '{file_storage_obj.filename}' enviado com sucesso para o bucket."
        )
    except Exception as e:
        return f"Erro ao enviar arquivo: {e}"


def list_files():
    storage_client = storage.Client()
    BUCKET_NAME = current_app.config["CLOUD_STORAGE_NAME"]

    try:
        bucket = storage_client.bucket(BUCKET_NAME)
        blobs = bucket.list_blobs()
        # Focar apenas em arquivos pdf por hora
        return [blob.name for blob in blobs if blob.name.endswith((".pdf"))]
    except Exception as e:
        return f"Erro ao carregar a listagem dos arquivo: {e}"


def download_file(filename, destination_path):
    storage_client = storage.Client()
    BUCKET_NAME = current_app.config["CLOUD_STORAGE_NAME"]

    try:
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(filename)
        blob.download_to_filename(destination_path)
    except Exception as e:
        return f"Erro ao baixar o arquivo {filename}: {e}"


def delete_file(file_name: str):
    storage_client = storage.Client()
    BUCKET_NAME = current_app.config["CLOUD_STORAGE_NAME"]

    try:
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(file_name)

        # Caso não encontre um arquivo com o nome indicado
        if not blob.exists():
            return f"Arquivo '{file_name}' não encontrado no bucket."

        blob.delete()
        return f"Arquivo '{file_name}' removido com sucesso do bucket."
    except Exception as e:
        return f"Erro ao deletar o arquivo '{file_name}': {e}"


def load_files_from_gcs(filenames: list[str] = None):
    available_files = list_files()
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
