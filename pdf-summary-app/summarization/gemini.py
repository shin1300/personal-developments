import os
import traceback
from dotenv import load_dotenv
from openai import OpenAI

# .env から APIキーを読み込み
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print("APIキーは読み込めていますか:", bool(api_key))

if not api_key:
    print("警告: OPENAI_API_KEY が設定されていません。")

# OpenAIクライアントの初期化
try:
    client = OpenAI()
except Exception as e:
    print("OpenAIクライアントの初期化に失敗しました。")
    print(traceback.format_exc())
    client = None

def gsummarize_text(text: str, max_tokens: int = 300) -> str:
    if client is None:
        return "OpenAIクライアントが初期化されていません。"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたは優秀な文章要約AIです。"},
                {"role": "user", "content": f"以下の文章を簡潔に要約してください。\n\n{text}"}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"OpenAI API error: {e}")
        print(traceback.format_exc())
        return "要約に失敗しました。"

if __name__ == "__main__":
    test_text = "人工知能とは、人間の知能をコンピューターで再現する技術である。"
    summary = summarize_text(test_text)
    print("要約結果:", summary)
