# 📘 PDF・Web 記事要約アプリ

## 🔍 概要

本プロジェクトは、**PDF ファイルや Web 記事の URL を入力することで、その内容を要約して返す AI アプリケーション**の開発を目的としています。  
ユーザーがアップロードした文章を OpenAI の GPT モデルを活用して効率よく短くまとめることで、情報の把握や共有を支援します。

---

## 🛠️ 主な機能

- PDF ファイルのテキスト抽出
- Web ページの本文抽出
- 長文の分割処理（チャンク化）
- OpenAI GPT API による要約生成
- シンプルな Web UI でのファイル・URL 入力と要約結果表示

---

## 📂 データ・入力例

- `data/sample.pdf`：テスト用のサンプル PDF ファイル
- URL 例：ニュース記事や技術ブログの URL を入力して要約可能

---

## 🛠 技術スタック

- Python 3.x
- PDF 解析：PyMuPDF (fitz)
- Web スクレイピング：requests + BeautifulSoup4
- 要約 AI：OpenAI GPT-4 / GPT-3.5 Turbo API
- Web アプリ：Streamlit または FastAPI + React（予定）
- 環境管理：requirements.txt、.env による API キー管理

---

## 📈 今後の拡張案

- 要約文の長さやスタイル調整機能
- キーワード抽出やトピック分類の追加
- 複数言語対応
- ユーザー認証・保存機能の実装

---

## 📌 開発のポイント

- PDF のテキスト抽出は PyMuPDF で実装（`extract_text/pdf_extractor.py`）
- Web 記事の本文抽出は BeautifulSoup で実装（`extract_text/web_extractor.py`）
- OpenAI API 呼び出しは`summarization/openai_api.py`にまとめる
- 環境変数で API キーを安全に管理（`.env`ファイル推奨）
- こまめなコミットと README 更新を心がける

---
