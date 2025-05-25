from flask_api.app import create_app

app = create_app()

if __name__ == "__main__":
    # 開発環境用にデバッグモードで起動
    app.run(debug=True)
