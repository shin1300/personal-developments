# 💻 personal-dev: 機械学習・時系列予測のポートフォリオ集

このリポジトリは、個人開発・研究で作成した複数の機械学習／時系列予測プロジェクトをまとめたポートフォリオです。  
各フォルダに独立したプロジェクトが含まれており、使用技術や目的に応じて整理されています。

---

## 📂 プロジェクト一覧

### [`lstm`](./lstm-temp-forecasting/)
**📘 適温予測モデル：スマートリング・赤外線アレイセンサによる体温データを用いて**

- スマートリング・赤外線アレイセンサ・室温センサから得られたデータを用いて、**主観的に心地よいと感じる温度（適温）**を予測
- 使用モデル：
  - XGBoost
  - LSTM
  - LSTM + XGBoost のハイブリッドモデル
- センサ構成：Omron D6T, Sensirion SHT31, Raspberry Pi Pico など
- 詳細は[`lstm-temp-forecasting/README.md`](./lstm-temp-forecasting/README.md) を参照

---

## 🛠 今後の追加予定
- 実験的な実装やKaggle参加コードなど
