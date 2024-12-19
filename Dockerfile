# ベースイメージを指定
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-jpn \
    libtesseract-dev \
    git \
    && apt-get clean

# Pythonライブラリの依存関係をコピーしてインストール
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install opencv-python-headless

# プロジェクトファイルをコンテナにコピー
COPY . .

# # アプリケーションのエントリポイント（必要に応じて修正）
# CMD ["python", "main.py"]
