from cohere import Client
import os

# Cohere APIクライアントの初期化（環境変数からAPIキーを取得）
co = Client(os.getenv("COHERE_API_KEY"))

def summarize_text(text, length="medium"):
    """
    指定したテキストをCohereの要約APIで要約する関数

    Args:
        text (str): 要約対象のテキスト
        length (str): 要約の長さ（"short", "medium", "long"）

    Returns:
        str: 要約結果の文章
    """
    response = co.summarize(
        text=text,
        length=length,
        format="paragraph",
        model="summarize-xlarge",
    )
    return response.summary
