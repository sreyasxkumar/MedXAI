import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    """
    Extracts text from each page of the uploaded PDF file.
    """
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()
