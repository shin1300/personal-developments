import streamlit as st
from utils.pdf_utils import extract_text_pdf
from utils.web_utils import extract_text_web
from utils.cohere_api import summarize_text

st.title("PDF・Web記事要約アプリ")

input_type = st.radio("入力タイプを選択", ["PDFアップロード", "Web記事URL"])

if input_type == "PDFアップロード":
    uploaded_file = st.file_uploader("PDFファイルをアップロード", type=["pdf"])
    if uploaded_file:
        text = extract_text_pdf(uploaded_file)
        summary = summarize_text(text)
        st.subheader("要約結果")
        st.write(summary)

else:
    url = st.text_input("Web記事URLを入力")
    if url:
        text = extract_text_web(url)
        summary = summarize_text(text)
        st.subheader("要約結果")
        st.write(summary)
