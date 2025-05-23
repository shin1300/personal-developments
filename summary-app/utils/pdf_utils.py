import fitz
from fpdf import FPDF
import io

def extract_text_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def create_pdf_from_text(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.split("\n"):
        pdf.cell(0, 10, line, ln=True)
    # バイト列としてPDFデータを取得
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    # BytesIOに変換して返す
    return io.BytesIO(pdf_bytes)
