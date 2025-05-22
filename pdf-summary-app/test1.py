from extract_text.pdf import extract_text_from_pdf
from extract_text.web import extract_text_from_url
from summarization.hft import hsummarize_text

def summarize_pdf(pdf_path: str):
    text = extract_text_from_pdf(pdf_path)
    summary = hsummarize_text(text)
    return summary

def summarize_web(url: str):
    text = extract_text_from_url(url)
    summary = hsummarize_text(text)
    return summary

if __name__ == "__main__":
    # PDF要約テスト
    pdf_path = "data/sample.pdf"
    print("=== PDF要約結果 ===")
    print(summarize_pdf(pdf_path))
    print()

    # Webページ要約テスト
    url = "https://ja.wikipedia.org/wiki/OpenAI"
    print("=== Webページ要約結果 ===")
    print(summarize_web(url))
