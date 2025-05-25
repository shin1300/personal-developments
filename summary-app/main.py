import streamlit as st
import requests
from utils.pdf_utils import extract_text_pdf, create_pdf_from_text
from utils.web_utils import extract_text_web
from utils.cohere_api import summarize_text
from utils.text_utils import split_text_into_chunks
from utils.api_post import post_summary_to_flask

MIN_LENGTH = 250
MAX_CHUNK_LENGTH = 5000

def summarize_long_text(text: str, length: str = "medium") -> str | None:
    """
    長文テキストをチャンク分割し、多段階で要約を行う。
    テキストが短すぎる場合は元のテキストを返す。
    """
    try:
        text_for_check = text.replace("\n", "").replace(" ", "")
        if len(text_for_check) < MIN_LENGTH:
            st.warning("テキストが短すぎるため要約できません。元のテキストを表示します。")
            return text

        if len(text) <= MAX_CHUNK_LENGTH:
            return summarize_text(text, length)

        chunks = split_text_into_chunks(text, max_length=MAX_CHUNK_LENGTH)
        st.info(f"{len(chunks)}個のチャンクに分割して要約します。")

        summaries = []
        for i, chunk in enumerate(chunks):
            with st.spinner(f"{i + 1}/{len(chunks)}個目のチャンクを要約中..."):
                summaries.append(summarize_text(chunk, length="medium"))

        intermediate_summary = "\n\n".join(summaries)
        st.info("全体要約を生成しています...")
        return summarize_text(intermediate_summary, length=length)

    except Exception as e:
        st.error(f"要約中にエラーが発生しました: {e}")
        return None

def show_summary_and_download(summary: str, original_text: str, source_type: str, source_info: str) -> None:
    """
    要約結果を表示し、TXT/PDFダウンロードボタンと保存ボタンを設置。
    """
    st.subheader("要約結果")
    st.write(summary)

    st.download_button(
        label="要約をTXTファイルでダウンロード",
        data=summary,
        file_name="summary.txt",
        mime="text/plain",
    )

    pdf_data = create_pdf_from_text(summary)
    st.download_button(
        label="要約をPDFファイルでダウンロード",
        data=pdf_data,
        file_name="summary.pdf",
        mime="application/pdf",
    )

    if st.button("要約を保存する"):
        result = post_summary_to_flask(
            input_text=original_text,
            summary_text=summary,
            source_type=source_type,
            source_info=source_info
        )
        st.success(result)

    with st.expander("原文を表示する"):
        st.write(original_text)

def show_saved_summaries() -> None:
    """
    保存済みの要約一覧を取得して表示。
    """
    st.header("保存済み要約一覧")

    try:
        response = requests.get("http://127.0.0.1:5000/summaries")
        response.raise_for_status()
        summaries = response.json()

        if not summaries:
            st.info("保存された要約はまだありません。")
            return

        for item in summaries:
            st.subheader(f"ID: {item['id']} - {item['source']} ({item['input_type']})")
            st.write(f"作成日時: {item['created_at']}")
            st.write(item['summary'])
            st.markdown("---")

    except Exception as e:
        st.error(f"保存済み要約の取得に失敗しました: {e}")

def main():
    st.title("PDF・Web記事要約アプリ")

    input_type = st.radio("入力タイプを選択", ["PDFアップロード", "Web記事URL"])
    length_label = st.radio("要約の長さを選択", ["短く", "中くらい", "詳しく"])
    length_map = {"短く": "short", "中くらい": "medium", "詳しく": "long"}
    selected_length = length_map[length_label]

    if input_type == "PDFアップロード":
        uploaded_file = st.file_uploader("PDFファイルをアップロード", type=["pdf"])
        if uploaded_file:
            try:
                with st.spinner("PDFを読み込んでいます..."):
                    text = extract_text_pdf(uploaded_file)

                with st.spinner("要約を生成中です..."):
                    summary = summarize_long_text(text, selected_length)

                if summary:
                    show_summary_and_download(summary, text, source_type="pdf", source_info=uploaded_file.name)

            except Exception as e:
                st.error(f"PDF読み込みまたは要約中にエラーが発生しました: {e}")

    else:
        url = st.text_input("Web記事URLを入力")
        if url:
            try:
                with st.spinner("Webページを読み込んでいます..."):
                    text = extract_text_web(url)

                with st.spinner("要約を生成中です..."):
                    summary = summarize_long_text(text, selected_length)

                if summary:
                    show_summary_and_download(summary, text, source_type="web", source_info=url)

            except Exception as e:
                st.error(f"Web記事読み込みまたは要約中にエラーが発生しました: {e}")

    if st.button("保存済み要約を見る"):
        show_saved_summaries()

if __name__ == "__main__":
    main()
