import requests
from bs4 import BeautifulSoup

def extract_text_web(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    paragraphs = soup.find_all("p")
    text = "\n".join(p.get_text() for p in paragraphs)
    return text