from PyPDF2 import PdfReader


def extract_text(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.strip()
    except Exception as e:
        raise RuntimeError(f"Erro ao extrair o texto do arquivo '{file_path}': {e}")
