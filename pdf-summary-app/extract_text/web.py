import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def extract_text_from_url(url: str) -> str:
    """Webページの本文テキストを抽出する（シンプル版）"""
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # 例として<p>タグのテキストを結合
    paragraphs = soup.find_all('p')
    text = "\n".join(p.get_text() for p in paragraphs)

    return text

if __name__ == "__main__":
    url = "https://ja.wikipedia.org/wiki/OpenAI"
    text = extract_text_from_url(url)
    print(text[:1000])  # 最初の1000文字だけ表示
