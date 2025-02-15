"""Configuration settings for the F1 SQL Analysis agents."""

import os
from pathlib import Path

# ************* Database Connection *************
# Dockerコンテナ内かどうかを判定
IN_DOCKER = os.path.exists('/.dockerenv')

# Docker環境では'pgvector'、それ以外では'localhost'を使用
DB_HOST = 'pgvector' if IN_DOCKER else 'localhost'

# ポート番号を設定（Docker環境では5432、それ以外ではPOSTGRES_PORT環境変数か5432）
DB_PORT = '5432' if IN_DOCKER else os.getenv('POSTGRES_PORT', '5432')

DB_URL = f"postgresql+psycopg://ai:ai@{DB_HOST}:{DB_PORT}/ai"

# ************* Paths *************
CWD = Path(__file__).parent.parent
KNOWLEDGE_DIR = CWD.joinpath("knowledge")
OUTPUT_DIR = CWD.joinpath("output")

# Create the output directory if it does not exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
