from PyPDF2 import PdfReader

def load_pdf(file_path):
    text = ""

    pdf = PdfReader(file_path)

    for page in pdf.pages:
        text += page.extract_text()

    return text