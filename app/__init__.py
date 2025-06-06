import os

from dotenv import load_dotenv
from flask import Flask

from .routes import bp


def create_app():
    load_dotenv()

    # Inicialização da API
    app = Flask(__name__)

    app.register_blueprint(bp)

    app.config["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
    app.config["CLOUD_STORAGE_NAME"] = os.getenv("CLOUD_STORAGE_NAME")

    # Definição de chave de acesso a serviços GCP
    cloud_key = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if cloud_key:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cloud_key
    else:
        raise RuntimeError("Chave json para GCP não definida")

    return app
