import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def extract_text_nhk(soup):
    """
    NHKニュースの記事本文抽出
    <div id="news_textbody">内の<p>タグを抽出
    """
    container = soup.find("div", id="news_textbody")
    if not container:
        return None
    paragraphs = container.find_all("p")
    texts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
    return "\n".join(texts) if texts else None

def extract_text_yahoo_news(soup):
    """
    Yahoo!ニュースの記事本文抽出
    <div class="newsFeed_item_body">内の<p>タグを抽出
    """
    container = soup.find("div", class_="newsFeed_item_body")
    if not container:
        return None
    paragraphs = container.find_all("p")
    texts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
    return "\n".join(texts) if texts else None

def extract_text_asahi(soup):
    """
    朝日新聞デジタルの記事本文抽出
    <div id="text">内の<p>タグを抽出
    """
    container = soup.find("div", id="text")
    if not container:
        return None
    paragraphs = container.find_all("p")
    texts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
    return "\n".join(texts) if texts else None

def extract_text_generic(soup):
    """
    汎用的な記事本文抽出
    ページ内の全ての<p>タグのテキストを結合
    """
    paragraphs = soup.find_all("p")
    texts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
    return "\n".join(texts) if texts else None

def extract_text_web(url):
    """
    URLからニュース記事の本文テキストを抽出する関数。
    対応サイト(NHK、Yahoo!ニュース、朝日新聞)は個別抽出処理を行い、
    それ以外は汎用抽出を行う。
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, "html.parser")

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

        # 対応サイト以外は汎用抽出
        return extract_text_generic(soup)

    except Exception as e:
        return f"エラーが発生しました: {e}"
