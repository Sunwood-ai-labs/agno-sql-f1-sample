#!/bin/bash
set -e

# F1データの読み込み
echo "🏁 F1データを読み込んでいます..."
python load_f1_data.py

# ナレッジベースの読み込み
echo "📚 ナレッジベースを読み込んでいます..."
python load_knowledge.py

# Streamlitアプリケーションを起動
echo "🚀 アプリケーションを起動しています..."
exec streamlit run app.py --server.address=0.0.0.0
