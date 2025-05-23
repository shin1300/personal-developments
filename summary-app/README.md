# 📘 PDF・Web 記事要約アプリ

## 🔍 概要

本プロジェクトは、**PDF ファイルや Web 記事の URL を入力することで、その内容を Cohere の生成 AI を用いて要約するアプリケーション**の開発を目的としています。  
ユーザーがアップロードした文章や Web から抽出したテキストを効率的に短くまとめ、情報の把握や共有を支援します。

## 🌐 対応している Web 記事について

本アプリは以下のような種類の Web 記事から本文テキストを抽出し、要約を行うことを想定しています。

- **ニュースサイト**  
  例：朝日新聞、NHK ニュース、Yahoo!ニュースなど  
  主要な記事本文を抽出し、広告やサイドバーなどの不要情報を除去して要約。

---

## 📁 ディレクトリ構成

```
summary-app/
│
├── main.py # Streamlitアプリのエントリーポイント
│
│
├── utils/                  # ユーティリティ関数まとめ
│   ├── __init__.py
│   ├── cohere_api.py       # Cohere要約API呼び出し関数
│   ├── pdf_utils.py        # PDFテキスト抽出用関数
│   ├── text_utils.py       # テキスト分割
│   └── web_utils.py        # Web記事テキスト抽出用関数
│
│
├── .gitignore
│
├── README.md # ← 今このファイル
│
└── requirements.txt # 必要なライブラリ
```

---

# 🛠️ 主な機能

- PDF ファイルのテキスト抽出（PyMuPDF 使用）
- Web ページの本文抽出（requests + BeautifulSoup 使用）
- Cohere 生成 AI API による要約生成
- 長文テキストのチャンク分割と多段階要約対応
- シンプルな Streamlit Web UI でのファイル・URL 入力と要約結果表示

---

## 🛠 使用技術

- Python 3.10
- PDF 解析：PyMuPDF (fitz)
- Web スクレイピング：requests + BeautifulSoup4
- 要約 AI：Cohere API（`summarize-xlarge`モデル）
- Web アプリ：Streamlit
- 環境管理：`requirements.txt`、環境変数による API キー管理

---

## 🧠 長文テキストの分割と多段階要約について

本アプリでは、長文のテキストを扱う際に以下の工夫をしています。

- **テキストのチャンク分割**  
  テキストが一定の長さ（例：5000 文字）を超える場合、全文をそのまま要約 API に投げると処理が重くなったり、API の文字数制限に引っかかるため、まず適切な長さに分割します。

- **分割チャンクごとの要約**  
  分割した各チャンクに対して個別に要約を実行します。

- **多段階要約（2 段階要約）**  
  チャンクごとの要約結果をさらにまとめて、最終的に全体を代表する要約文を生成します。  
  これにより、単にチャンクを並べただけではなく、文章全体の構造や要点を反映したグローバルな要約が可能になります。

- **短文テキストの処理**  
  テキストが非常に短い場合は要約を行わず、元のテキストをそのまま表示します。

このような処理で、大量の文章でも効率よく、かつ質の高い要約を提供できるよう設計しています。

---

## 📌 開発のポイント

- PDF テキスト抽出は`utils/pdf_utils.py`にて PyMuPDF で実装
- Web 記事本文抽出は`utils/web_utils.py`にて requests+BeautifulSoup で実装
- Cohere API 呼び出しは`utils/cohere_api.py`にまとめ、環境変数で API キーを管理
- 長文テキストは`main.py`内でチャンク分割し、**多段階要約（チャンクごと要約＋再要約）**を行う実装
- Streamlit の UI は`main.py`にまとめ、ファイルアップロード・URL 入力から要約表示までを実装

---

## 📌 実行方法

```bash
# 1. 仮想環境作成
python -m venv myenv
myenv\Scripts\activate

# 2. パッケージインストール
pip install -r requirements.txt

# 3. 環境変数にAPIキー設定
$env:COHERE_API_KEY="あなたのAPIキー"

# 4. アプリ起動
streamlit run main.py
```
