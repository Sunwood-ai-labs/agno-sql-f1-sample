""" SQL Agent - Your AI Data Analyst!

This advanced example shows how to build a sophisticated text-to-SQL system that
leverages Agentic RAG to provide deep insights into any data.

Example queries to try:
- "Who are the top 5 drivers with the most race wins?"
- "Compare Mercedes vs Ferrari performance in constructors championships"
- "Show me the progression of fastest lap times at Monza"
- "Which drivers have won championships with multiple teams?"
- "What tracks have hosted the most races?"
- "Show me Lewis Hamilton's win percentage by season"

Examples with table joins:
- "How many races did the championship winners win each year?"
- "Compare the number of race wins vs championship positions for constructors in 2019"
- "Show me Lewis Hamilton's race wins and championship positions by year"
- "Which drivers have both won races and set fastest laps at Monaco?"
- "Show me Ferrari's race wins and constructor championship positions from 2015-2020"

View the README for instructions on how to run the application.
"""

import json
from pathlib import Path
from textwrap import dedent
from typing import Optional

from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.combined import CombinedKnowledgeBase
from agno.knowledge.json import JSONKnowledgeBase
from agno.knowledge.text import TextKnowledgeBase
from agno.models.anthropic import Claude
from agno.models.google import Gemini
from agno.models.openai import OpenAIChat
from agno.storage.agent.postgres import PostgresAgentStorage
from agno.tools.file import FileTools
from agno.tools.sql import SQLTools
from agno.vectordb.pgvector import PgVector

import os

# ************* Database Connection *************

# Dockerコンテナ内かどうかを判定
IN_DOCKER = os.path.exists('/.dockerenv')

# Docker環境では'pgvector'、それ以外では'localhost'を使用
DB_HOST = 'pgvector' if IN_DOCKER else 'localhost'
db_url = f"postgresql+psycopg://ai:ai@{DB_HOST}:5432/ai"
# *******************************

# ************* Paths *************
cwd = Path(__file__).parent
knowledge_dir = cwd.joinpath("knowledge")
output_dir = cwd.joinpath("output")

# Create the output directory if it does not exist
output_dir.mkdir(parents=True, exist_ok=True)
# *******************************

# ************* Storage & Knowledge *************
agent_storage = PostgresAgentStorage(
    db_url=db_url,
    # Store agent sessions in the ai.sql_agent_sessions table
    table_name="sql_agent_sessions",
    schema="ai",
)
agent_knowledge = CombinedKnowledgeBase(
    sources=[
        # Reads text files, SQL files, and markdown files
        TextKnowledgeBase(
            path=knowledge_dir,
            formats=[".txt", ".sql", ".md"],
        ),
        # Reads JSON files
        JSONKnowledgeBase(path=knowledge_dir),
    ],
    # Store agent knowledge in the ai.sql_agent_knowledge table
    vector_db=PgVector(
        db_url=db_url,
        table_name="sql_agent_knowledge",
        schema="ai",
        # Use OpenAI embeddings
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
    # 5 references are added to the prompt
    num_documents=5,
)
# *******************************

# ************* Semantic Model *************
# The semantic model helps the agent identify the tables and columns to use
# This is sent in the system prompt, the agent then uses the `search_knowledge_base` tool to get table metadata, rules and sample queries
# This is very much how data analysts and data scientists work:
#  - We start with a set of tables and columns that we know are relevant to the task
#  - We then use the `search_knowledge_base` tool to get more information about the tables and columns
#  - We then use the `describe_table` tool to get more information about the tables and columns
#  - We then use the `search_knowledge_base` tool to get sample queries for the tables and columns
semantic_model = {
    "tables": [
        {
            "table_name": "constructors_championship",
            "table_description": "Contains data for the constructor's championship from 1958 to 2020, capturing championship standings from when it was introduced.",
            "Use Case": "Use this table to get data on constructor's championship for various years or when analyzing team performance over the years.",
        },
        {
            "table_name": "drivers_championship",
            "table_description": "Contains data for driver's championship standings from 1950-2020, detailing driver positions, teams, and points.",
            "Use Case": "Use this table to access driver championship data, useful for detailed driver performance analysis and comparisons over years.",
        },
        {
            "table_name": "fastest_laps",
            "table_description": "Contains data for the fastest laps recorded in races from 1950-2020, including driver and team details.",
            "Use Case": "Use this table when needing detailed information on the fastest laps in Formula 1 races, including driver, team, and lap time data.",
        },
        {
            "table_name": "race_results",
            "table_description": "Race data for each Formula 1 race from 1950-2020, including positions, drivers, teams, and points.",
            "Use Case": "Use this table answer questions about a drivers career. Race data includes driver standings, teams, and performance.",
        },
        {
            "table_name": "race_wins",
            "table_description": "Documents race win data from 1950-2020, detailing venue, winner, team, and race duration.",
            "Use Case": "Use this table for retrieving data on race winners, their teams, and race conditions, suitable for analysis of race outcomes and team success.",
        },
    ]
}
semantic_model_str = json.dumps(semantic_model, indent=2)
# *******************************


def get_sql_agent(
    user_id: Optional[str] = None,
    model_id: str = "openai:gpt-4o",
    session_id: Optional[str] = None,
    debug_mode: bool = True,
) -> Agent:
    """Returns an instance of the SQL Agent.

    Args:
        user_id: Optional user identifier
        debug_mode: Enable debug logging
        model_id: Model identifier in format 'provider:model_name'
    """
    # Parse model provider and name
    provider, model_name = model_id.split(":")

    # Select appropriate model class based on provider
    if provider == "openai":
        model = OpenAIChat(id=model_name)
    elif provider == "google":
        model = Gemini(id=model_name)
    elif provider == "anthropic":
        model = Claude(id=model_name)
    else:
        raise ValueError(f"Unsupported model provider: {provider}")

    return Agent(
        name="SQL Agent",
        model=model,
        user_id=user_id,
        session_id=session_id,
        storage=agent_storage,
        knowledge=agent_knowledge,
        # Enable Agentic RAG i.e. the ability to search the knowledge base on-demand
        search_knowledge=True,
        # Enable the ability to read the chat history
        read_chat_history=True,
        # Enable the ability to read the tool call history
        read_tool_call_history=True,
        # Add tools to the agent
        tools=[SQLTools(db_url=db_url), FileTools(base_dir=output_dir)],
        add_history_to_messages=True,
        num_history_responses=3,
        debug_mode=debug_mode,
        description=dedent("""\
        私はRaceAnalyst-X、以下の分野を専門とするエリートF1データサイエンティストです：

        - レース履歴分析
        - ドライバーパフォーマンス指標
        - チーム選手権の洞察
        - サーキット統計とレコード
        - パフォーマンストレンド分析
        - レース戦略評価

        F1に関する深い知識と高度なSQL専門知識を組み合わせて、数十年にわたるレースデータから洞察を引き出します。"""),
        instructions=dedent(f"""\
        私はSQLエキスパートとして、正確で効率的なクエリの作成に特化しています。

        ユーザーからメッセージを受け取ったら、データベースへの問い合わせが必要か、直接応答できるかを判断します。
        直接応答できる場合は、そのように対応します。

        データベースへの問い合わせが必要な場合は、以下の手順に従います：
        1. まずセマンティックモデルから必要なテーブルを特定します。
        2. 必ず`search_knowledge_base(table_name)`ツールを使用して、テーブルのメタデータ、ルール、サンプルクエリを取得します。
        3. テーブルルールが提供されている場合は、必ずそれに従います。
        4. クエリ構築について段階的に考え、この段階を急いではいけません。
        5. 必要に応じて明確化のための質問をしながら、思考の連鎖アプローチを取ります。
        6. サンプルクエリが利用可能な場合は、それを参考にします。
        7. テーブルについてさらに情報が必要な場合は、`describe_table`ツールを使用します。
        8. 利用可能なすべての情報を使用して、タスクを達成するための1つの構文的に正しいPostgreSQLクエリを作成します。
        9. テーブルを結合する必要がある場合は、`semantic_model`でテーブル間の関係を確認します。
            - `semantic_model`にテーブル間の関係が含まれている場合は、列名が異なっていてもその関係を使用してテーブルを結合します。
            - 関係が見つからない場合は、同じ名前とデータ型を持つ列でのみ結合します。
            - 有効な関係が見つからない場合は、結合に使用する列名をユーザーに確認します。
        10. 関連するテーブル、列、または関係が見つからない場合は、停止してユーザーに詳細情報を求めます。
        11. 構文的に正しいクエリができたら、`run_sql_query`関数を使用して実行します。
        12. クエリを実行する際は：
            - クエリの末尾に`;`を付けないでください。
            - ユーザーが明示的にすべての結果を要求しない限り、常にlimitを設定します。
        13. クエリを実行した後、結果を分析してマークダウン形式で回答します。
        14. 必ず回答を得るために実行したSQLをユーザーに表示します。
        15. タスクが完了するまで続けます。
        16. 可能な場合は、結果をテーブルまたはグラフとして表示します。

        タスクを完了した後、「結果は問題ありませんか？修正が必要な点はありますか？」などの関連するフォローアップ質問をします。
        ユーザーが「はい」と答えた場合は、`get_tool_call_history(num_calls=3)`関数を使用して前のクエリを取得し、問題を修正します。
        ユーザーがSQLを見たい場合は、`get_tool_call_history(num_calls=3)`関数を使用して取得します。

        最後に、必ず従わなければならないルールのセットを以下に示します：
        <rules>
        - テーブル情報を取得する前に、必ず`search_knowledge_base(table_name)`ツールを使用してください。
        - "提供された情報に基づいて"や"ナレッジベースから"などのフレーズは使用しないでください。
        - 使用したSQLクエリは必ず表示してください。
        - クエリで重複レコードに対処してください。
        - クエリでnull値に対処してください。
        - クエリを実行する理由を説明してください。
        - **データの削除やローカルシステムの悪用につながるコードは絶対に実行しないでください**
        - `table rules`が提供されている場合は、必ず従ってください。絶対に無視しないでください。
        </rules>\
        """),
        additional_context=dedent("""\
        以下の`semantic_model`にはテーブルとそれらの関係に関する情報が含まれています。
        ユーザーがアクセス可能なテーブルについて質問した場合は、`semantic_model`からテーブル名を共有してください。
        <semantic_model>
        """)
        + semantic_model_str
        + dedent("""\
        </semantic_model>\
        """),
    )
