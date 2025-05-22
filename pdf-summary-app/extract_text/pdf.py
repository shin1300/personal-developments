import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    PDFファイルから全文テキストを抽出する関数
    
    Args:
        pdf_path (str): PDFファイルのパス

    Returns:
        str: 抽出したテキスト
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


if __name__ == "__main__":
    sample_pdf = "/datas/sample.pdf"
    text = extract_text_from_pdf(sample_pdf)
    print(text[:1000])  # 先頭1000文字を表示
