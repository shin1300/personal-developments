import requests

def post_summary_to_flask(input_text, summary_text, source_type, source_info=None):
    """
    FlaskバックエンドAPIに要約データをPOSTして保存する関数

    Parameters:
    ----------
    input_text : str
        要約対象の元テキスト（現状未使用だが将来拡張可能）
    summary_text : str
        生成された要約テキスト
    source_type : str
        入力タイプ（例: 'PDF', 'Web記事'など）
    source_info : str, optional
        要約元の情報（例: URLやファイル名など）

    Returns:
    -------
    str
        保存結果のメッセージ（成功・失敗・エラー内容）
    """

    url = "http://localhost:5000/save"
    payload = {
        "input_type": source_type,
        "source": source_info,
        "summary": summary_text,
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 201:
            return "✅ 保存成功"
        else:
            return f"⚠️ 保存失敗: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"❌ エラー: {e}"
