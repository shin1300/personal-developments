# 📘 PDF・Web 記事要約アプリ

## 🔍 概要

本プロジェクトは、**PDF ファイルや Web 記事の URL を入力することで、その内容を Cohere の生成 AI を用いて要約するアプリケーション**の開発を目的としています。  
ユーザーがアップロードした文章や Web から抽出したテキストを効率的に短くまとめ、情報の把握や共有を支援します。

---

## 🛠️ 主な機能

- PDF ファイルのテキスト抽出（PyMuPDF 使用）
- Web ページの本文抽出（requests + BeautifulSoup 使用）
- Cohere 生成 AI API による要約生成
- シンプルな Streamlit Web UI でのファイル・URL 入力と要約結果表示

---

## 📂 データ・入力例

- テスト用 PDF ファイル（例：`data/sample.pdf`など）
- ニュース記事や技術ブログの URL を入力して要約可能

---

## 🛠 技術スタック

- Python 3.10
- PDF 解析：PyMuPDF (fitz)
- Web スクレイピング：requests + BeautifulSoup4
- 要約 AI：Cohere API（`summarize-xlarge`モデル）
- Web アプリ：Streamlit
- 環境管理：`requirements.txt`、環境変数による API キー管理（`.env`推奨）

---

## 📈 今後の拡張案

- 入力テキストの分割（チャンク化）対応と長文処理の強化
- 要約文の長さやトーン調整機能の追加
- キーワード抽出やトピック分類機能の実装
- 複数言語対応の検討
- ユーザー認証や履歴保存機能の実装
- デプロイ（Heroku、Vercel、Streamlit Cloud など）

---

## 📌 開発のポイント

- PDF テキスト抽出は`utils/pdf_utils.py`にて PyMuPDF で実装
- Web 記事本文抽出は`utils/web_utils.py`にて requests+BeautifulSoup で実装
- Cohere API 呼び出しは`utils/cohere_api.py`にまとめ、環境変数で API キーを管理
- Streamlit の UI は`main.py`にまとめ、ファイルアップロード・URL 入力から要約表示までを一気通貫で実装
- API キーは`.env`ファイル等で安全に管理し、Git 管理から除外
- こまめなコミットで機能単位での履歴を残す

---

## 📌 実行方法

```bash
# 1. 仮想環境作成（推奨）
python3 -m venv venv
source venv/bin/activate  # Windowsは venv\Scripts\activate

# 2. パッケージインストール
pip install -r requirements.txt

# 3. 環境変数にAPIキー設定
export COHERE_API_KEY="あなたのAPIキー"
# Windows PowerShellの場合
# $env:COHERE_API_KEY="あなたのAPIキー"

# 4. アプリ起動
streamlit run main.py
```
