<div align="center">

![SQL Agent Header](https://github.com/user-attachments/assets/a3979ece-da40-492c-87a2-e52b56c9f7e2)

# Agno SQL F1 sample

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Agno](https://img.shields.io/badge/Framework-Agno-purple)](https://docs.agno.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-brightgreen)](https://openai.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)](https://www.postgresql.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.41-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

[![GitHub stars](https://img.shields.io/github/stars/Sunwood-ai-labs/agno-sql-f1-sample?style=social)](https://github.com/Sunwood-ai-labs/agno-sql-f1-sample/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Sunwood-ai-labs/agno-sql-f1-sample?style=social)](https://github.com/Sunwood-ai-labs/agno-sql-f1-sample/network/members)

</div>

このサンプルプロジェクトは、Agentic RAGを活用して高度なテキストからSQLへの変換システムを構築する方法を示しています。F1（フォーミュラ1）のデータセットを例として使用していますが、このシステムは他のデータセットにも容易に拡張できるように設計されています。

このエージェントはAgentic RAGを使用してテーブルのメタデータとルールを検索し、より良いSQLクエリを作成・実行することができます。

> [!NOTE]
> 必要に応じてリポジトリをフォークしてクローンしてください。

## 🚀 クイックスタート

### Docker Composeで起動

1. 環境変数の設定
```bash
# .envファイルを作成し、必要なAPIキーを設定
cp .env.example .env
# 以下のAPIキーを.envファイルに設定してください
# - OPENAI_API_KEY（必須）
# - ANTHROPIC_API_KEY（オプション）
# - GOOGLE_API_KEY（オプション）
# - GROQ_API_KEY（オプション）
```

2. アプリケーションの起動
```bash
docker compose up -d
```

これだけで以下のサービスが自動的に起動します：
- PostgreSQL (pgvector): `localhost:5532`でアクセス可能
- SQLエージェントUI: `localhost:8509`でアクセス可能

> [!NOTE]
> - 初回起動時は、F1データとナレッジベースの読み込みが自動的に行われます
> - データの読み込みには数分かかる場合があります

3. アプリケーションの停止
```bash
docker compose down
```

データを完全に削除する場合：
```bash
docker compose down -v
```

## 💬 サポート

質問がある場合は[Discord](https://agno.link/discord)でお問い合わせください。

## 🛠️ 技術スタック

- [Agno](https://docs.agno.com) - 軽量なマルチモーダルエージェントフレームワーク
  - シンプルな設計：グラフやチェーンを使用せず、純粋なPythonで実装
  - 高性能：最小限のメモリフットプリントで高速なエージェント実行
  - モデル非依存：任意のモデル、プロバイダー、モダリティに対応
  - マルチモーダル：テキスト、画像、音声、動画のネイティブサポート
  - マルチエージェント：専門化されたエージェント間でのタスク委譲
  - メモリ管理：ユーザーセッションとエージェントの状態をデータベースに保存
  - ナレッジストア：Agentic RAGまたは動的few-shotのためのベクトルデータベース
  - 構造化出力：エージェントが構造化データで応答
  - モニタリング：エージェントのセッションとパフォーマンスをリアルタイムで追跡
- Python 3.9+
- OpenAI GPT-4
- PostgreSQL 16 (pgvector)
- Streamlit 1.41
- Docker

## 📄 ライセンス

このプロジェクトは[MIT License](LICENSE)の下で公開されています。
