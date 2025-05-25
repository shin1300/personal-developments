import requests

def post_summary_to_flask(input_text, summary_text, source_type, source_info=None):
    url = "http://localhost:5000/save"
    payload = {
        "input_type": source_type,    # Flaskの input_type に対応
        "source": source_info,        # Flaskの source に対応
        "summary": summary_text       # Flaskの summary に対応
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 201:
            return "✅ 保存成功"
        else:
            return f"⚠️ 保存失敗: {response.text}"
    except Exception as e:
        return f"❌ エラー: {e}"
