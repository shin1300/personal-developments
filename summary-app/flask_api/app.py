from flask import Flask
from flask_api.extensions import db

def create_app():
    app = Flask(__name__)

    # PostgreSQL データベースの接続設定
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Shintaro130@localhost/summarydb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # トラッキング機能の無効化（パフォーマンス向上）

    # 拡張機能の初期化
    db.init_app(app)

    with app.app_context():
        # ルートやモデルのインポート（循環参照回避のため関数内に記述）
        from flask_api import routes
        # テーブル作成（初回のみ）
        db.create_all()

    return app
