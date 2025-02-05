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

## 🚀 セットアップ手順

### 🌱 1. 仮想環境の作成

```shell
python3 -m venv .venv
source .venv/bin/activate
```

### 📦 2. ライブラリのインストール

```shell
pip install -r cookbook/examples/apps/sql_agent/requirements.txt
```

### 🐳 3. PgVectorの実行

データの保存にはPostgresを使用しますが、SQLエージェントは任意のデータベースで動作します。

> 最初に[docker desktop](https://docs.docker.com/desktop/install/mac-install/)をインストールしてください。

- ヘルパースクリプトを使用して実行

```shell
./cookbook/run_pgvector.sh
```

- または docker run コマンドを使用して実行

```shell
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  agnohq/pgvector:16
```

### 🏎️ 4. F1データの読み込み

```shell
python cookbook/examples/apps/sql_agent/load_f1_data.py
```

### 📚 5. ナレッジベースの読み込み

ナレッジベースには、テーブルのメタデータ、ルール、サンプルクエリが含まれており、エージェントはこれらを使用してより良い応答を生成します。

以下の項目を必要に応じて追加することをお勧めします：
  - テーブルメタデータに`table_rules`と`column_rules`を追加します。エージェントはこれらのルールに従うように設計されています。特定の形式で日付を照会したり、特定のカラムを避けたりする場合に便利です。
  - `cookbook/use_cases/apps/sql_agent/knowledge_base/sample_queries.sql`ファイルにサンプルSQLクエリを追加します。これにより、アシスタントは複雑なクエリの作成方法を学習できます。

```shell
python cookbook/examples/apps/sql_agent/load_knowledge.py
```

### 🔑 6. APIキーのエクスポート

このタスクにはgpt-4oの使用を推奨しますが、任意のモデルを使用することができます。

```shell
export OPENAI_API_KEY=***
```

他のAPIキーはオプションですが、テストする場合は以下を設定してください：

```shell
export ANTHROPIC_API_KEY=***
export GOOGLE_API_KEY=***
export GROQ_API_KEY=***
```

### 🚀 7. SQLエージェントの実行

```shell
streamlit run cookbook/examples/apps/sql_agent/app.py
```

- [localhost:8501](http://localhost:8501)を開いてSQLエージェントを表示します。

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
