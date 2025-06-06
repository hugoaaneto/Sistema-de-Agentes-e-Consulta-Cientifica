from flask import Blueprint, request, jsonify

from app.agents.orchestrator_agent import initialize_orchestrate_agent
from app.services.cloud_storage import upload_file

bp = Blueprint("api", __name__)


@bp.route("/chatbot", methods=["POST"])
def handle_chatbot_message():
    # O usuario pode enviar apenas um arquivo, apenas uma mensagem ou os dois
    message = request.form.get("message")
    file = request.files.get("file")

    response = {}

    if file and file.filename:
        response["file_response"] = upload_file(file)

    if message:
        response["message_response"] = initialize_orchestrate_agent(message)

    if not response:
        return (
            jsonify({"error": "Envie ao menos um dos campos: 'message' ou 'file'"}),
            400,
        )

    return jsonify(response)
