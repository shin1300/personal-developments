import fitz
from fpdf import FPDF
import io


def extract_text_pdf(pdf_file):
    """
    PDFファイルからテキストを抽出する関数。

    Args:
        pdf_file: アップロードされたPDFファイルオブジェクト

    Returns:
        テキスト文字列
    """
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def create_pdf_from_text(text):
    """
    テキストからPDFファイルを作成し、BytesIOオブジェクトで返す関数。

    Args:
        text: PDFに変換するテキスト文字列

    Returns:
        BytesIOオブジェクト（PDFデータ）
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for line in text.split("\n"):
        pdf.cell(0, 10, line, ln=True)

    # PDFをバイト列として取得しBytesIOに変換
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    return io.BytesIO(pdf_bytes)
