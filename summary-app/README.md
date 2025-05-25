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
├── flask_api/ # Flask + PostgreSQL バックエンドAPI
│   ├── __init__.py
│   ├── app.py # Flaskアプリ作成ファイル
│   ├── run.py # Flaskアプリの起動スクリプト
│   ├── models.py # SQLAlchemyモデル定義
│   ├── routes.py # APIエンドポイント定義
│   └── extensions.py # DB拡張機能
│
├──migrations/
│   ├── env.py               # マイグレーション環境の設定ファイル
│   ├── versions/            # 各バージョンごとのスクリプトが入る
│   ├── README               # マイグレーションの概要説明
│   ├── script.py.mako       # 自動生成用テンプレート
│   └── alembic.ini          # Alembic設定ファイル
│
│
├── .gitignore
│
├── README.md # ← 今このファイル
│
└── requirements.txt # 必要なライブラリ
```

---

# ✅ 主な機能

- PDF ファイルのテキスト抽出（PyMuPDF 使用）
- Web ページの本文抽出（requests + BeautifulSoup 使用）
- Cohere 生成 AI API による要約生成
- 長文テキストのチャンク分割と多段階要約対応
- シンプルな Streamlit Web UI でのファイル・URL 入力と要約結果表示
- Streamlit による直感的な UI でファイル・URL の入力、要約表示、ダウンロード
- 要約結果の Flask API 経由でのデータベース保存機能

---

## 🛠 使用技術

- 言語：Python 3.10
- PDF 解析：PyMuPDF（`fitz`）
- Web スクレイピング：`requests` + `BeautifulSoup4`
- 自然言語処理：Cohere API（`summarize-xlarge`モデルによる要約）
- フロントエンド：Streamlit
- バックエンド：Flask（REST API 構築）
- データベース：PostgreSQL（SQLAlchemy による操作）

---

## 🧠 長文テキストの分割と多段階要約について

本アプリでは、長文のテキストを扱う際に以下の工夫をしています。

- **テキストのチャンク分割・要約**  
  テキストが一定の長さ（例：5000 文字）を超える場合、全文をそのまま要約 API に投げると処理が重くなったり、API の文字数制限に引っかかるため、まず適切な長さに分割します。
  分割した各チャンクに対して個別に要約を実行します。

- **多段階要約（2 段階要約）**  
  チャンクごとの要約結果をさらにまとめて、最終的に全体を代表する要約文を生成します。  
  これにより、単にチャンクを並べただけではなく、文章全体の構造や要点を反映したグローバルな要約が可能になります。

- **短文テキストの処理**  
  テキストが非常に短い場合は要約を行わず、元のテキストをそのまま表示します。

このような処理で、大量の文章でも効率よく、かつ質の高い要約を提供できるよう設計しています。

---

## 📌 開発のポイント（フロントエンド & バックエンド）

### 🔹 フロントエンド（Streamlit）

- **PDF テキスト抽出**は `utils/pdf_utils.py` にて PyMuPDF を使用して実装
- **Web 記事本文の抽出**は `utils/web_utils.py` にて **requests + BeautifulSoup** により実装
- **Cohere API の呼び出し**は `utils/cohere_api.py` に集約し、環境変数で API キーを安全に管理
- 長文テキストのチャンク分割と多段階要約処理は `main.py` 内で実装
- Streamlit UI は `main.py` に集約し、ファイルアップロード・URL 入力・要約表示・要約保存までを提供

### 🔹 バックエンド（Flask + PostgreSQL）

- Flask アプリは `flask_api/app.py` で Factory パターンを用いて構築
- SQLAlchemy モデル定義は `flask_api/models.py` に記述し、要約履歴を DB に保存
- API エンドポイントは `flask_api/routes.py` にまとめ、`/save` で POST 受け取り可能
- PostgreSQL データベースとの接続は `flask_api/extensions.py` に定義された `SQLAlchemy` インスタンスで管理
- アプリ起動スクリプトは `flask_api/run.py` により実行
