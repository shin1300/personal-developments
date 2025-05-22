from transformers import pipeline

# 要約パイプラインの初期化（小型モデルならすぐ起動します）
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def hsummarize_text(text: str, max_length=150, min_length=40) -> str:
    """
    テキストを要約する関数
    max_length, min_lengthで要約の長さを調整可能
    """
    summary_list = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary_list[0]['summary_text']


if __name__ == "__main__":
    sample_text = (
        "Hugging Face社のTransformersライブラリは、"
        "自然言語処理における最先端のモデルを簡単に利用できるように設計されています。"
        "特に要約タスクではBARTやT5モデルがよく使われています。"
    )
    print("=== 要約結果 ===")
    print(summarize_text(sample_text))
