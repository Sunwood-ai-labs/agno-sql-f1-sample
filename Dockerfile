FROM python:3.11-slim

WORKDIR /app

# システムの依存関係をインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Pythonパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコピー
COPY . .

# custum agnoをインストール
RUN pip install git+https://github.com/Sunwood-ai-labs/agno.git#subdirectory=libs/agno

# 実行時の環境変数を設定
ENV PYTHONUNBUFFERED=1

# Streamlitのポートを公開
EXPOSE 8501

# entrypointスクリプトをコピーして実行可能に
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]
