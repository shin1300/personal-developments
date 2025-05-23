import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def extract_text_nhk(soup):
    container = soup.find("div", id="news_textbody")
    if not container:
        return None
    paragraphs = container.find_all("p")
    texts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
    return "\n".join(texts) if texts else None

def extract_text_yahoo_news(soup):
    # Yahoo!ニュースは <div class="newsFeed_item_body"> に記事本文が入っていることが多い
    container = soup.find("div", class_="newsFeed_item_body")
    if not container:
        return None
    paragraphs = container.find_all("p")
    texts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
    return "\n".join(texts) if texts else None

def extract_text_asahi(soup):
    # 朝日新聞デジタルは <div id="text"> の中に本文がまとまっていることが多い
    container = soup.find("div", id="text")
    if not container:
        return None
    paragraphs = container.find_all("p")
    texts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
    return "\n".join(texts) if texts else None

def extract_text_generic(soup):
    paragraphs = soup.find_all("p")
    texts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
    return "\n".join(texts) if texts else None

def extract_text_web(url):
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, "html.parser")

        domain = urlparse(url).netloc.lower()

        if "nhk.or.jp" in domain:
            text = extract_text_nhk(soup)
            if text:
                return text

        elif "news.yahoo.co.jp" in domain or "yahoo.co.jp" in domain:
            text = extract_text_yahoo_news(soup)
            if text:
                return text

        elif "asahi.com" in domain:
            text = extract_text_asahi(soup)
            if text:
                return text

        # 対応していない場合は汎用抽出
        return extract_text_generic(soup)

    except Exception as e:
        return f"エラーが発生しました: {e}"
