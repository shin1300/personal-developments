from flask_api.extensions import db
from datetime import datetime

class Summary(db.Model):
    __tablename__ = 'summaries'  # 明示的にテーブル名を指定

    id = db.Column(db.Integer, primary_key=True)
    input_type = db.Column(db.String(20), nullable=False)  # 入力タイプ
    source = db.Column(db.Text, nullable=False)            # 元のテキストやURLなど
    summary = db.Column(db.Text, nullable=False)           # 要約結果
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # 作成日時

    def __repr__(self):
        return f"<Summary id={self.id} input_type={self.input_type}>"
