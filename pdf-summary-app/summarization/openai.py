import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
print("APIキーは読み込めていますか:", os.getenv("OPENAI_API_KEY"))
client = OpenAI()

def osummarize_text(text: str, max_tokens: int = 300) -> str:
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
        return "要約に失敗しました。"
