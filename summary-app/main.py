import streamlit as st
from utils.pdf_utils import extract_text_pdf
from utils.web_utils import extract_text_web
from utils.cohere_api import summarize_text
from utils.text_utils import split_text_into_chunks
from utils.pdf_utils import create_pdf_from_text  # PDF作成関数を追加読み込み

MIN_LENGTH = 250  # 要約APIが受け付ける最小文字数

# 長文テキストを分割して順に要約する関数
def summarize_long_text(text, length="medium"):
    try:
        text_for_check = text.replace("\n", "").replace(" ", "")
        if len(text_for_check) < MIN_LENGTH:
            st.warning("テキストが短すぎるため要約できません。元のテキストを表示します。")
            return text

        MAX_LENGTH = 5000
        if len(text) <= MAX_LENGTH:
            return summarize_text(text, length)

        chunks = split_text_into_chunks(text, max_length=MAX_LENGTH)
        st.info(f"{len(chunks)}個のチャンクに分割して要約します。")

        summaries = []
        for i, chunk in enumerate(chunks):
            with st.spinner(f"{i+1}/{len(chunks)}個目のチャンクを要約中..."):
                summaries.append(summarize_text(chunk, length="medium"))

        intermediate_summary = "\n\n".join(summaries)
        st.info("全体要約を生成しています...")
        return summarize_text(intermediate_summary, length=length)

    except Exception as e:
        st.error(f"要約中にエラーが発生しました: {e}")
        return None


# アプリタイトル
st.title("PDF・Web記事要約アプリ")

# 入力タイプ選択（PDFまたはWeb）
input_type = st.radio("入力タイプを選択", ["PDFアップロード", "Web記事URL"])

# 要約の長さを選択
length_label = st.radio("要約の長さを選択", ["短く", "中くらい", "詳しく"])
length_map = {"短く": "short", "中くらい": "medium", "詳しく": "long"}
selected_length = length_map[length_label]

def show_summary_and_download(summary, original_text):
    st.subheader("要約結果")
    st.write(summary)

    # ダウンロードボタン（TXT）
    st.download_button(
        label="要約をTXTファイルでダウンロード",
        data=summary,
        file_name="summary.txt",
        mime="text/plain",
    )

    # ダウンロードボタン（PDF）
    pdf_data = create_pdf_from_text(summary)
    st.download_button(
        label="要約をPDFファイルでダウンロード",
        data=pdf_data,
        file_name="summary.pdf",
        mime="application/pdf",
    )

    with st.expander("原文を表示する"):
        st.write(original_text)


# PDFファイルアップロード処理
if input_type == "PDFアップロード":
    uploaded_file = st.file_uploader("PDFファイルをアップロード", type=["pdf"])
    if uploaded_file:
        try:
            with st.spinner("PDFを読み込んでいます..."):
                text = extract_text_pdf(uploaded_file)

            with st.spinner("要約を生成中です..."):
                summary = summarize_long_text(text, selected_length)

            if summary:
                show_summary_and_download(summary, text)

        except Exception as e:
            st.error(f"PDF読み込みまたは要約中にエラーが発生しました: {e}")

# Web記事URL入力処理
else:
    url = st.text_input("Web記事URLを入力")
    if url:
        try:
            with st.spinner("Webページを読み込んでいます..."):
                text = extract_text_web(url)

            with st.spinner("要約を生成中です..."):
                summary = summarize_long_text(text, selected_length)

            if summary:
                show_summary_and_download(summary, text)

        except Exception as e:
            st.error(f"Web記事読み込みまたは要約中にエラーが発生しました: {e}")
