from app.services.cloud_storage import load_files_documents

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from flask import current_app


def retrieve_relevant_passages(query: str):
    # Carregamento de arquivos
    documents = load_files_documents()

    # Divide os textos em chuncks
    splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=64)
    split_docs = splitter.split_documents(documents)

    # Para o RAG deixei o embedding fixo no gemini, mas poderia ser adaptado para ser dinamico de forma semelhante ao motor dos agentes
    embedding_model = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=current_app.config["GEMINI_API_KEY"],
    )

    # Banco vetorial
    vectorstore = Chroma.from_documents(documents=split_docs, embedding=embedding_model)

    # Busca vetorial
    docs = vectorstore.similarity_search(query, k=5)

    return f"Para a query '{query}' foram identificadas as seguintes informações relevantes:\n\n".join(
        [doc.page_content for doc in docs]
    )
