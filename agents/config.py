"""Configuration settings for the F1 SQL Analysis agents."""

import os
from pathlib import Path

# ************* Database Connection *************
# Dockerコンテナ内かどうかを判定
IN_DOCKER = os.path.exists('/.dockerenv')

# Docker環境では'pgvector'、それ以外では'localhost'を使用
DB_HOST = 'pgvector' if IN_DOCKER else 'localhost'
DB_URL = f"postgresql+psycopg://ai:ai@{DB_HOST}:5432/ai"

# ************* Paths *************
CWD = Path(__file__).parent.parent
KNOWLEDGE_DIR = CWD.joinpath("knowledge")
OUTPUT_DIR = CWD.joinpath("output")

# Create the output directory if it does not exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
