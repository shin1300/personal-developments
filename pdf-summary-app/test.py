
import os
import traceback
from dotenv import load_dotenv
import google.generativeai as genai

# .env から APIキーを読み込み
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print("APIキーは読み込めていますか:", bool(api_key))

if not api_key:
    print("警告: GEMINI_API_KEY が設定されていません。")

# Gemini API設定
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")  # ← list_models() で確認した名前に変更！
except Exception as e:
    print("Geminiモデルの初期化に失敗しました。")
    print(traceback.format_exc())
    model = None

def gsummarize_text(text: str) -> str:
    if model is None:
        return "Geminiクライアントが初期化されていません。"

    try:
        prompt = f"以下の文章を簡潔に要約してください。\n\n{text}"
        response = model.generate_content(prompt)
        print("API応答:", response.text)
        return response.text.strip()
    except Exception as e:
        print(f"Gemini API error: {e}")
        print(traceback.format_exc())
        return "要約に失敗しました。"

if __name__ == "__main__":
    test_text = "人工知能とは、人間の知能をコンピューターで再現する技術である。"
    summary = gsummarize_text(test_text)
    print("要約結果:", summary)
