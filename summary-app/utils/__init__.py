#extract_text/__init__.py から見て、同じフォルダにある web_extractor.py をインポート
from .pdf_utils import extract_text_pdf
from .web_utils import extract_text_web
