from flask import request, jsonify
from flask_api.extensions import db
from flask_api.models import Summary
from flask import current_app as app

@app.route("/save", methods=["POST"])
def save_summary():
    data = request.get_json()
    print("Received JSON:", data)

    input_type = data.get("input_type")
    source = data.get("source")
    summary_text = data.get("summary")

    if not summary_text:
        print("No summary provided!")
        return jsonify({"error": "No summary provided"}), 400

    new_summary = Summary(input_type=input_type, source=source, summary=summary_text)
    db.session.add(new_summary)
    db.session.commit()

    return jsonify({"message": "Summary saved successfully"}), 201

@app.route("/", methods=["GET"])
def index():
    # トップページ用など。必要なければ削除してください。
    return jsonify({"message": "Welcome to the summary app"}), 200

@app.route("/summaries", methods=["GET"])
def get_summaries():
    summaries = Summary.query.order_by(Summary.created_at.desc()).all()
    result = [
        {
            "id": s.id,
            "input_type": s.input_type,
            "source": s.source,
            "summary": s.summary,
            "created_at": s.created_at.isoformat()
        }
        for s in summaries
    ]
    return jsonify(result), 200
