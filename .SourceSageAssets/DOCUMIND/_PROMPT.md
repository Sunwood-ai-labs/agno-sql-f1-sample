
以下の情報を元に、リリースノートの要件に従ってSourceSageの新バージョンv0.2.0の日本語のリリースノートを生成してください。

# リリースノートの要件:
<Release notes requirements>

1. 各項目に関連するコミットハッシュがある場合は、(commit: abc1234のように)括弧内に記載してください。ハッシュは最初の7文字のみ使用してください。
2. 重要な変更や注意が必要な点があれば、別セクションで強調してください。
3. アップグレード手順や互換性に関する注意事項があれば記載してください。
4. 貢献者への謝辞を含めてください（もし情報があれば）。
5. 各セクションに適切な絵文字を使用して、視覚的に分かりやすくしてください。
6. 完成されたマークダウン形式のリリースノートを作成してください。
7. 各項目の末尾に、その情報の確信度を 🟢（高）、🟡（中）、🔴（低）で示してください。
8. 提供された情報のみを使用し、推測や一般化された情報の追加は避けてください。
9. 情報が不足している場合は、その旨を明記し、該当するセクションを省略してください。
9. 既に機能が実装されておりアップデートのような項目は、「🔄」と明記してください。
10. ステップバイステップで正確に処理してください
11. ハルシネーションが起きないようにしてください
12. 特に情報が無いセクションは記載しないで省略して。

</Release notes requirements>

# 絵文字の使用ガイドライン:
<Emoji usage guidelines>
- 新機能: 🎉 (パーティーポッパー)
- 改善点: 🚀 (ロケット)
- バグ修正: 🐛 (バグ)
- 重要な変更: ⚠️ (警告)
- セキュリティ関連: 🔒 (鍵)
- パフォーマンス改善: ⚡ (稲妻)
- ドキュメント: 📚 (本)
- 非推奨: 🗑️ (ゴミ箱)
- 削除された機能: 🔥 (炎)
- 確信度（高）: 🟢
- 確信度（中）: 🟡
- 確信度（低）: 🔴
- 継続中の項目: 🔄
</Emoji usage guidelines>

# リリースノートのフォーマット:
<Release notes format>
# 🚀 SourceSage vv0.2.0 リリースノート

## 📋 概要
[全体的な変更の要約と主要なハイライトを1-2文で]

## ✨ 新機能
- 🎉 [新機能の説明] (commit: xxxxxxx) 🟢🟡🔴 🔄
    - [詳細な説明]

## 🛠 改善点
- 🚀 [改善点の説明] (commit: xxxxxxx) 🟢🟡🔴 🔄
    - [詳細な説明]
    
## 🐛 バグ修正
- 🐛 [修正されたバグの説明] (commit: xxxxxxx) 🟢🟡🔴 🔄
    - [詳細な説明]

## ⚠️ 重要な変更
- ⚠️ [重要な変更点や注意が必要な点] 🟢🟡🔴 🔄
    - [詳細な説明]
    
## 📦 アップグレード手順
[必要に応じてアップグレード手順や注意事項を記載]

## 👏 謝辞
[貢献者への謝辞]
</Release notes format>

# 入力情報:
<Input information>

## 今回のリリースの変更履歴
<change history>

</change history>

## [参考資料] リポジトリの全体情報
下記にはリポジトリの構造とリポジトリ内の主要なファイルの一覧を記載します。
リリースノートを作成時の事前知識として参考に使用して

<Repository information>
    # Project: sql_agent

```plaintext
OS: posix
Directory: /home/maki/prj/agno/cookbook/examples/apps/sql_agent

├── knowledge/
│   ├── constructors_championship.json
│   ├── drivers_championship.json
│   ├── fastest_laps.json
│   ├── race_results.json
│   ├── race_wins.json
│   └── sample_queries.sql
├── .SourceSageignore
├── __init__.py
├── agents.py
├── app.py
├── generate_requirements.sh
├── load_f1_data.py
├── load_knowledge.py
├── README.md
├── requirements.in
├── requirements.txt
└── utils.py
```

## 📊 プロジェクト統計

- 📅 作成日時: 2025-02-05 11:35:46
- 📁 総ディレクトリ数: 1
- 📄 総ファイル数: 17
- 📏 最大深度: 1
- 📦 最大ディレクトリ:  (18 エントリ)

### 📊 ファイルサイズと行数

| ファイル | サイズ | 行数 | 言語 |
|----------|--------|------|------|
| agents.py | 11.3 KB | 237 | python |
| utils.py | 9.5 KB | 294 | python |
| app.py | 6.4 KB | 167 | python |
| requirements.txt | 3.4 KB | 187 | plaintext |
| README.md | 2.4 KB | 91 | markdown |
| knowledge/race_results.json | 1.7 KB | 61 | json |
| load_f1_data.py | 1.6 KB | 50 | python |
| knowledge/sample_queries.sql | 1.5 KB | 69 | sql |
| knowledge/drivers_championship.json | 1.3 KB | 46 | json |
| knowledge/race_wins.json | 1.3 KB | 47 | json |
| knowledge/fastest_laps.json | 1.0 KB | 41 | json |
| knowledge/constructors_championship.json | 957.0 B | 31 | json |
| .SourceSageignore | 599.0 B | 46 | plaintext |
| generate_requirements.sh | 466.0 B | 12 | bash |
| load_knowledge.py | 303.0 B | 12 | python |
| requirements.in | 89.0 B | 9 | plaintext |
| __init__.py | 0.0 B | 0 | python |
| **合計** |  | **1400** |  |

### 📈 言語別統計

| 言語 | ファイル数 | 総行数 | 合計サイズ |
|------|------------|--------|------------|
| python | 6 | 760 | 29.0 KB |
| plaintext | 3 | 242 | 4.1 KB |
| json | 5 | 226 | 6.2 KB |
| markdown | 1 | 91 | 2.4 KB |
| sql | 1 | 69 | 1.5 KB |
| bash | 1 | 12 | 466.0 B |

`.SourceSageignore`

**サイズ**: 599.0 B | **行数**: 46 行
```plaintext
# バージョン管理システム関連
.git/
.gitignore

# キャッシュファイル
__pycache__/
.pytest_cache/
**/__pycache__/**
*.pyc

# ビルド・配布関連
build/
dist/
*.egg-info/

# 一時ファイル・出力
output/
output.md
test_output/
.SourceSageAssets/
.SourceSageAssetsDemo/

# アセット
*.png
*.svg
*.jpg
*.jepg
assets/

# その他
LICENSE
example/
package-lock.json
.DS_Store

# 特定のディレクトリを除外
tests/temp/
docs/drafts/

# パターンの例外（除外対象から除外）
!docs/important.md
!.github/workflows/
repository_summary.md

venv
.venv
```

`README.md`

**サイズ**: 2.4 KB | **行数**: 91 行
```markdown
# SQL Agent

This advanced example shows how to build a sophisticated text-to-SQL system that leverages Agentic RAG to provide deep insights into any data. We'll use the F1 dataset as an example, but the system is designed to be easily extensible to other datasets.

The agent uses Agentic RAG to search for table metadata and rules, enabling it to write and run better SQL queries.

> Note: Fork and clone the repository if needed

### 1. Create a virtual environment

```shell
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install libraries

```shell
pip install -r cookbook/examples/apps/sql_agent/requirements.txt
```

### 3. Run PgVector

Let's use Postgres for storing our data, but the SQL Agent should work with any database.

> Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) first.

- Run using a helper script

```shell
./cookbook/run_pgvector.sh
```

- OR run using the docker run command

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

### 4. Load F1 data

```shell
python cookbook/examples/apps/sql_agent/load_f1_data.py
```

### 5. Load the knowledge base

The knowledge base contains table metadata, rules and sample queries, which are used by the Agent to improve responses.

We recommend adding the following as you go along:
  - Add `table_rules` and `column_rules` to the table metadata. The Agent is prompted to follow them. This is useful when you want to guide the Agent to always query date in a particular format, or avoid certain columns.
  - Add sample SQL queries to the `cookbook/use_cases/apps/sql_agent/knowledge_base/sample_queries.sql` file. This will give the Assistant a head start on how to write complex queries.

```shell
python cookbook/examples/apps/sql_agent/load_knowledge.py
```

### 6. Export API Keys

We recommend using gpt-4o for this task, but you can use any Model you like.

```shell
export OPENAI_API_KEY=***
```

Other API keys are optional, but if you'd like to test:

```shell
export ANTHROPIC_API_KEY=***
export GOOGLE_API_KEY=***
export GROQ_API_KEY=***
```

### 7. Run SQL Agent

```shell
streamlit run cookbook/examples/apps/sql_agent/app.py
```

- Open [localhost:8501](http://localhost:8501) to view the SQL Agent.

### 8. Message us on [discord](https://agno.link/discord) if you have any questions
```

`__init__.py`

**サイズ**: 0.0 B | **行数**: 0 行
```python
(Empty file)
```

`agents.py`

**サイズ**: 11.3 KB | **行数**: 237 行
```python
"""🏎️ SQL Agent - Your AI Data Analyst!

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

# ************* Database Connection *************
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
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
        You are RaceAnalyst-X, an elite Formula 1 Data Scientist specializing in:

        - Historical race analysis
        - Driver performance metrics
        - Team championship insights
        - Track statistics and records
        - Performance trend analysis
        - Race strategy evaluation

        You combine deep F1 knowledge with advanced SQL expertise to uncover insights from decades of racing data."""),
        instructions=dedent(f"""\
        You are a SQL expert focused on writing precise, efficient queries.

        When a user messages you, determine if you need query the database or can respond directly.
        If you can respond directly, do so.

        If you need to query the database to answer the user's question, follow these steps:
        1. First identify the tables you need to query from the semantic model.
        2. Then, ALWAYS use the `search_knowledge_base(table_name)` tool to get table metadata, rules and sample queries.
        3. If table rules are provided, ALWAYS follow them.
        4. Then, think step-by-step about query construction, don't rush this step.
        5. Follow a chain of thought approach before writing SQL, ask clarifying questions where needed.
        6. If sample queries are available, use them as a reference.
        7. If you need more information about the table, use the `describe_table` tool.
        8. Then, using all the information available, create one single syntactically correct PostgreSQL query to accomplish your task.
        9. If you need to join tables, check the `semantic_model` for the relationships between the tables.
            - If the `semantic_model` contains a relationship between tables, use that relationship to join the tables even if the column names are different.
            - If you cannot find a relationship in the `semantic_model`, only join on the columns that have the same name and data type.
            - If you cannot find a valid relationship, ask the user to provide the column name to join.
        10. If you cannot find relevant tables, columns or relationships, stop and ask the user for more information.
        11. Once you have a syntactically correct query, run it using the `run_sql_query` function.
        12. When running a query:
            - Do not add a `;` at the end of the query.
            - Always provide a limit unless the user explicitly asks for all results.
        13. After you run the query, analyse the results and return the answer in markdown format.
        14. Always show the user the SQL you ran to get the answer.
        15. Continue till you have accomplished the task.
        16. Show results as a table or a chart if possible.

        After finishing your task, ask the user relevant followup questions like "was the result okay, would you like me to fix any problems?"
        If the user says yes, get the previous query using the `get_tool_call_history(num_calls=3)` function and fix the problems.
        If the user wants to see the SQL, get it using the `get_tool_call_history(num_calls=3)` function.

        Finally, here are the set of rules that you MUST follow:
        <rules>
        - Use the `search_knowledge_base(table_name)` tool to get table information from your knowledge base before writing a query.
        - Do not use phrases like "based on the information provided" or "from the knowledge base".
        - Always show the SQL queries you use to get the answer.
        - Make sure your query accounts for duplicate records.
        - Make sure your query accounts for null values.
        - If you run a query, explain why you ran it.
        - **NEVER, EVER RUN CODE TO DELETE DATA OR ABUSE THE LOCAL SYSTEM**
        - ALWAYS FOLLOW THE `table rules` if provided. NEVER IGNORE THEM.
        </rules>\
        """),
        additional_context=dedent("""\
        The following `semantic_model` contains information about tables and the relationships between them.
        If the users asks about the tables you have access to, simply share the table names from the `semantic_model`.
        <semantic_model>
        """)
        + semantic_model_str
        + dedent("""\
        </semantic_model>\
        """),
        # Set to True to display tool calls in the response message
        # show_tool_calls=True,
    )
```

`app.py`

**サイズ**: 6.4 KB | **行数**: 167 行
```python
import nest_asyncio
import streamlit as st
from agents import get_sql_agent
from agno.agent import Agent
from agno.utils.log import logger
from utils import (
    CUSTOM_CSS,
    about_widget,
    add_message,
    display_tool_calls,
    rename_session_widget,
    session_selector_widget,
    sidebar_widget,
)

nest_asyncio.apply()

# Page configuration
st.set_page_config(
    page_title="F1 SQL Agent",
    page_icon=":checkered_flag:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load custom CSS with dark mode support
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def main() -> None:
    ####################################################################
    # App header
    ####################################################################
    st.markdown("<h1 class='main-title'>F1 SQL Agent</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='subtitle'>Your intelligent F1 data analyst powered by Agno</p>",
        unsafe_allow_html=True,
    )

    ####################################################################
    # Model selector
    ####################################################################
    model_options = {
        "gpt-4o": "openai:gpt-4o",
        "gemini-2.0-flash-exp": "google:gemini-2.0-flash-exp",
        "claude-3-5-sonnet": "anthropic:claude-3-5-sonnet-20241022",
    }
    selected_model = st.sidebar.selectbox(
        "Select a model",
        options=list(model_options.keys()),
        index=0,
        key="model_selector",
    )
    model_id = model_options[selected_model]

    ####################################################################
    # Initialize Agent
    ####################################################################
    sql_agent: Agent
    if (
        "sql_agent" not in st.session_state
        or st.session_state["sql_agent"] is None
        or st.session_state.get("current_model") != model_id
    ):
        logger.info("---*--- Creating new SQL agent ---*---")
        sql_agent = get_sql_agent(model_id=model_id)
        st.session_state["sql_agent"] = sql_agent
        st.session_state["current_model"] = model_id
    else:
        sql_agent = st.session_state["sql_agent"]

    ####################################################################
    # Load Agent Session from the database
    ####################################################################
    try:
        st.session_state["sql_agent_session_id"] = sql_agent.load_session()
    except Exception:
        st.warning("Could not create Agent session, is the database running?")
        return

    ####################################################################
    # Load runs from memory
    ####################################################################
    agent_runs = sql_agent.memory.runs
    if len(agent_runs) > 0:
        logger.debug("Loading run history")
        st.session_state["messages"] = []
        for _run in agent_runs:
            if _run.message is not None:
                add_message(_run.message.role, _run.message.content)
            if _run.response is not None:
                add_message("assistant", _run.response.content, _run.response.tools)
    else:
        logger.debug("No run history found")
        st.session_state["messages"] = []

    ####################################################################
    # Sidebar
    ####################################################################
    sidebar_widget()

    ####################################################################
    # Get user input
    ####################################################################
    if prompt := st.chat_input("👋 Ask me about F1 data from 1950 to 2020!"):
        add_message("user", prompt)

    ####################################################################
    # Display chat history
    ####################################################################
    for message in st.session_state["messages"]:
        if message["role"] in ["user", "assistant"]:
            _content = message["content"]
            if _content is not None:
                with st.chat_message(message["role"]):
                    # Display tool calls if they exist in the message
                    if "tool_calls" in message and message["tool_calls"]:
                        display_tool_calls(st.empty(), message["tool_calls"])
                    st.markdown(_content)

    ####################################################################
    # Generate response for user message
    ####################################################################
    last_message = (
        st.session_state["messages"][-1] if st.session_state["messages"] else None
    )
    if last_message and last_message.get("role") == "user":
        question = last_message["content"]
        with st.chat_message("assistant"):
            # Create container for tool calls
            tool_calls_container = st.empty()
            resp_container = st.empty()
            with st.spinner("🤔 Thinking..."):
                response = ""
                try:
                    # Run the agent and stream the response
                    run_response = sql_agent.run(question, stream=True)
                    for _resp_chunk in run_response:
                        # Display tool calls if available
                        if _resp_chunk.tools and len(_resp_chunk.tools) > 0:
                            display_tool_calls(tool_calls_container, _resp_chunk.tools)

                        # Display response
                        if _resp_chunk.content is not None:
                            response += _resp_chunk.content
                            resp_container.markdown(response)

                    add_message("assistant", response, sql_agent.run_response.tools)
                except Exception as e:
                    error_message = f"Sorry, I encountered an error: {str(e)}"
                    add_message("assistant", error_message)
                    st.error(error_message)

    ####################################################################
    # Session selector
    ####################################################################
    session_selector_widget(sql_agent, model_id)
    rename_session_widget(sql_agent)

    ####################################################################
    # About section
    ####################################################################
    about_widget()


if __name__ == "__main__":
    main()
```

`generate_requirements.sh`

**サイズ**: 466.0 B | **行数**: 12 行
```bash
#!/bin/bash

############################################################################
# Generate requirements.txt from requirements.in
############################################################################

echo "Generating requirements.txt"

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

UV_CUSTOM_COMPILE_COMMAND="./generate_requirements.sh" \
  uv pip compile ${CURR_DIR}/requirements.in --no-cache --upgrade -o ${CURR_DIR}/requirements.txt
```

`load_f1_data.py`

**サイズ**: 1.6 KB | **行数**: 50 行
```python
from io import StringIO

import pandas as pd
import requests
from agents import db_url
from agno.utils.log import logger
from sqlalchemy import create_engine

s3_uri = "https://agno-public.s3.amazonaws.com/f1"

# List of files and their corresponding table names
files_to_tables = {
    f"{s3_uri}/constructors_championship_1958_2020.csv": "constructors_championship",
    f"{s3_uri}/drivers_championship_1950_2020.csv": "drivers_championship",
    f"{s3_uri}/fastest_laps_1950_to_2020.csv": "fastest_laps",
    f"{s3_uri}/race_results_1950_to_2020.csv": "race_results",
    f"{s3_uri}/race_wins_1950_to_2020.csv": "race_wins",
}


def load_f1_data():
    """Load F1 data into the database"""

    logger.info("Loading database.")
    engine = create_engine(db_url)

    # Load each CSV file into the corresponding PostgreSQL table
    for file_path, table_name in files_to_tables.items():
        logger.info(f"Loading {file_path} into {table_name} table.")
        # Download the file using requests
        response = requests.get(file_path, verify=False)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Read the CSV data from the response content
        csv_data = StringIO(response.text)
        df = pd.read_csv(csv_data)

        df.to_sql(table_name, engine, if_exists="replace", index=False)
        logger.info(f"{file_path} loaded into {table_name} table.")

    logger.info("Database loaded.")


if __name__ == "__main__":
    # Disable SSL verification warnings
    import urllib3

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    load_f1_data()
```

`load_knowledge.py`

**サイズ**: 303.0 B | **行数**: 12 行
```python
from agents import agent_knowledge
from agno.utils.log import logger


def load_knowledge(recreate: bool = True):
    logger.info("Loading SQL agent knowledge.")
    agent_knowledge.load(recreate=recreate)
    logger.info("SQL agent knowledge loaded.")


if __name__ == "__main__":
    load_knowledge()
```

`requirements.in`

**サイズ**: 89.0 B | **行数**: 9 行
```plaintext
agno
openai
pandas
pgvector
psycopg[binary]
simplejson
sqlalchemy
streamlit
nest_asyncio
```

`requirements.txt`

**サイズ**: 3.4 KB | **行数**: 187 行
```plaintext
# This file was autogenerated by uv via the following command:
#    ./generate_requirements.sh
agno==0.1.2
    # via -r cookbook/examples/apps/sql/requirements.in
altair==5.5.0
    # via streamlit
annotated-types==0.7.0
    # via pydantic
anyio==4.8.0
    # via
    #   httpx
    #   openai
attrs==25.1.0
    # via
    #   jsonschema
    #   referencing
blinker==1.9.0
    # via streamlit
cachetools==5.5.1
    # via streamlit
certifi==2024.12.14
    # via
    #   httpcore
    #   httpx
    #   requests
charset-normalizer==3.4.1
    # via requests
click==8.1.8
    # via
    #   streamlit
    #   typer
distro==1.9.0
    # via openai
docstring-parser==0.16
    # via agno
gitdb==4.0.12
    # via gitpython
gitpython==3.1.44
    # via
    #   agno
    #   streamlit
h11==0.14.0
    # via httpcore
httpcore==1.0.7
    # via httpx
httpx==0.28.1
    # via
    #   agno
    #   openai
idna==3.10
    # via
    #   anyio
    #   httpx
    #   requests
jinja2==3.1.5
    # via
    #   altair
    #   pydeck
jiter==0.8.2
    # via openai
jsonschema==4.23.0
    # via altair
jsonschema-specifications==2024.10.1
    # via jsonschema
markdown-it-py==3.0.0
    # via rich
markupsafe==3.0.2
    # via jinja2
mdurl==0.1.2
    # via markdown-it-py
narwhals==1.24.0
    # via altair
nest-asyncio==1.6.0
    # via -r cookbook/examples/apps/sql/requirements.in
numpy==2.2.2
    # via
    #   pandas
    #   pgvector
    #   pydeck
    #   streamlit
openai==1.60.1
    # via -r cookbook/examples/apps/sql/requirements.in
packaging==24.2
    # via
    #   altair
    #   streamlit
pandas==2.2.3
    # via
    #   -r cookbook/examples/apps/sql/requirements.in
    #   streamlit
pgvector==0.3.6
    # via -r cookbook/examples/apps/sql/requirements.in
pillow==11.1.0
    # via streamlit
protobuf==5.29.3
    # via streamlit
psycopg==3.2.4
    # via -r cookbook/examples/apps/sql/requirements.in
psycopg-binary==3.2.4
    # via psycopg
pyarrow==19.0.0
    # via streamlit
pydantic==2.10.6
    # via
    #   agno
    #   openai
    #   pydantic-settings
pydantic-core==2.27.2
    # via pydantic
pydantic-settings==2.7.1
    # via agno
pydeck==0.9.1
    # via streamlit
pygments==2.19.1
    # via rich
python-dateutil==2.9.0.post0
    # via pandas
python-dotenv==1.0.1
    # via
    #   agno
    #   pydantic-settings
python-multipart==0.0.20
    # via agno
pytz==2024.2
    # via pandas
pyyaml==6.0.2
    # via agno
referencing==0.36.2
    # via
    #   jsonschema
    #   jsonschema-specifications
requests==2.32.3
    # via streamlit
rich==13.9.4
    # via
    #   agno
    #   streamlit
    #   typer
rpds-py==0.22.3
    # via
    #   jsonschema
    #   referencing
shellingham==1.5.4
    # via typer
simplejson==3.19.3
    # via -r cookbook/examples/apps/sql/requirements.in
six==1.17.0
    # via python-dateutil
smmap==5.0.2
    # via gitdb
sniffio==1.3.1
    # via
    #   anyio
    #   openai
sqlalchemy==2.0.37
    # via -r cookbook/examples/apps/sql/requirements.in
streamlit==1.41.1
    # via -r cookbook/examples/apps/sql/requirements.in
tenacity==9.0.0
    # via streamlit
toml==0.10.2
    # via streamlit
tomli==2.2.1
    # via agno
tornado==6.4.2
    # via streamlit
tqdm==4.67.1
    # via openai
typer==0.15.1
    # via agno
typing-extensions==4.12.2
    # via
    #   agno
    #   altair
    #   anyio
    #   openai
    #   psycopg
    #   pydantic
    #   pydantic-core
    #   referencing
    #   sqlalchemy
    #   streamlit
    #   typer
tzdata==2025.1
    # via pandas
urllib3==2.3.0
    # via requests
```

`utils.py`

**サイズ**: 9.5 KB | **行数**: 294 行
```python
from typing import Any, Dict, List, Optional

import streamlit as st
from agents import get_sql_agent
from agno.agent.agent import Agent
from agno.utils.log import logger


def load_data_and_knowledge():
    """Load F1 data and knowledge base if not already done"""
    from load_f1_data import load_f1_data
    from load_knowledge import load_knowledge

    if "data_loaded" not in st.session_state:
        with st.spinner("🔄 Loading data into database..."):
            load_f1_data()
        with st.spinner("📚 Loading knowledge base..."):
            load_knowledge()
        st.session_state["data_loaded"] = True
        st.success("✅ Data and knowledge loaded successfully!")


def add_message(
    role: str, content: str, tool_calls: Optional[List[Dict[str, Any]]] = None
) -> None:
    """Safely add a message to the session state"""
    if "messages" not in st.session_state or not isinstance(
        st.session_state["messages"], list
    ):
        st.session_state["messages"] = []
    st.session_state["messages"].append(
        {"role": role, "content": content, "tool_calls": tool_calls}
    )


def restart_agent():
    """Reset the agent and clear chat history"""
    logger.debug("---*--- Restarting agent ---*---")
    st.session_state["sql_agent"] = None
    st.session_state["sql_agent_session_id"] = None
    st.session_state["messages"] = []
    st.rerun()


def export_chat_history():
    """Export chat history as markdown"""
    if "messages" in st.session_state:
        chat_text = "# F1 SQL Agent - Chat History\n\n"
        for msg in st.session_state["messages"]:
            role = "🤖 Assistant" if msg["role"] == "agent" else "👤 User"
            chat_text += f"### {role}\n{msg['content']}\n\n"
        return chat_text
    return ""


def display_tool_calls(tool_calls_container, tools):
    """Display tool calls in a streamlit container with expandable sections.

    Args:
        tool_calls_container: Streamlit container to display the tool calls
        tools: List of tool call dictionaries containing name, args, content, and metrics
    """
    with tool_calls_container.container():
        for tool_call in tools:
            _tool_name = tool_call.get("tool_name")
            _tool_args = tool_call.get("tool_args")
            _content = tool_call.get("content")
            _metrics = tool_call.get("metrics")

            with st.expander(
                f"🛠️ {_tool_name.replace('_', ' ').title()}", expanded=False
            ):
                if isinstance(_tool_args, dict) and "query" in _tool_args:
                    st.code(_tool_args["query"], language="sql")

                if _tool_args and _tool_args != {"query": None}:
                    st.markdown("**Arguments:**")
                    st.json(_tool_args)

                if _content:
                    st.markdown("**Results:**")
                    try:
                        st.json(_content)
                    except Exception as e:
                        st.markdown(_content)

                if _metrics:
                    st.markdown("**Metrics:**")
                    st.json(_metrics)


def sidebar_widget() -> None:
    """Display a sidebar with sample user queries"""
    with st.sidebar:
        # Basic Information
        st.markdown("#### 🏎️ Basic Information")
        if st.button("📋 Show Tables"):
            add_message("user", "Which tables do you have access to?")
        if st.button("ℹ️ Describe Tables"):
            add_message("user", "Tell me more about these tables.")

        # Statistics
        st.markdown("#### 🏆 Statistics")
        if st.button("🥇 Most Race Wins"):
            add_message("user", "Which driver has the most race wins?")

        if st.button("🏆 Constructor Champs"):
            add_message("user", "Which team won the most Constructors Championships?")

        if st.button("⏳ Longest Career"):
            add_message(
                "user",
                "Tell me the name of the driver with the longest racing career? Also tell me when they started and when they retired.",
            )

        # Analysis
        st.markdown("#### 📊 Analysis")
        if st.button("📈 Races per Year"):
            add_message("user", "Show me the number of races per year.")

        if st.button("🔍 Team Performance"):
            add_message(
                "user",
                "Write a query to identify the drivers that won the most races per year from 2010 onwards and the position of their team that year.",
            )

        # Utility buttons
        st.markdown("#### 🛠️ Utilities")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 New Chat"):
                restart_agent()
        with col2:
            if st.download_button(
                "💾 Export Chat",
                export_chat_history(),
                file_name="f1_chat_history.md",
                mime="text/markdown",
            ):
                st.success("Chat history exported!")

        if st.sidebar.button("🚀 Load Data & Knowledge"):
            load_data_and_knowledge()


def session_selector_widget(agent: Agent, model_id: str) -> None:
    """Display a session selector in the sidebar"""

    if agent.storage:
        agent_sessions = agent.storage.get_all_sessions()
        # Get session names if available, otherwise use IDs
        session_options = []
        for session in agent_sessions:
            session_id = session.session_id
            session_name = (
                session.session_data.get("session_name", None)
                if session.session_data
                else None
            )
            display_name = session_name if session_name else session_id
            session_options.append({"id": session_id, "display": display_name})

        # Display session selector
        selected_session = st.sidebar.selectbox(
            "Session",
            options=[s["display"] for s in session_options],
            key="session_selector",
        )
        # Find the selected session ID
        selected_session_id = next(
            s["id"] for s in session_options if s["display"] == selected_session
        )

        if st.session_state["sql_agent_session_id"] != selected_session_id:
            logger.info(
                f"---*--- Loading {model_id} run: {selected_session_id} ---*---"
            )
            st.session_state["sql_agent"] = get_sql_agent(
                model_id=model_id,
                session_id=selected_session_id,
            )
            st.rerun()


def rename_session_widget(agent: Agent) -> None:
    """Rename the current session of the agent and save to storage"""

    container = st.sidebar.container()
    session_row = container.columns([3, 1], vertical_alignment="center")

    # Initialize session_edit_mode if needed
    if "session_edit_mode" not in st.session_state:
        st.session_state.session_edit_mode = False

    with session_row[0]:
        if st.session_state.session_edit_mode:
            new_session_name = st.text_input(
                "Session Name",
                value=agent.session_name,
                key="session_name_input",
                label_visibility="collapsed",
            )
        else:
            st.markdown(f"Session Name: **{agent.session_name}**")

    with session_row[1]:
        if st.session_state.session_edit_mode:
            if st.button("✓", key="save_session_name", type="primary"):
                if new_session_name:
                    agent.rename_session(new_session_name)
                    st.session_state.session_edit_mode = False
                    container.success("Renamed!")
        else:
            if st.button("✎", key="edit_session_name"):
                st.session_state.session_edit_mode = True


def about_widget() -> None:
    """Display an about section in the sidebar"""
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ℹ️ About")
    st.sidebar.markdown("""
    This SQL Assistant helps you analyze Formula 1 data from 1950 to 2020 using natural language queries.

    Built with:
    - 🚀 Agno
    - 💫 Streamlit
    """)


CUSTOM_CSS = """
    <style>
    /* Main Styles */
    .main-title {
        text-align: center;
        background: linear-gradient(45deg, #FF4B2B, #FF416C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3em;
        font-weight: bold;
        padding: 1em 0;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2em;
    }
    .stButton button {
        width: 100%;
        border-radius: 20px;
        margin: 0.2em 0;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .chat-container {
        border-radius: 15px;
        padding: 1em;
        margin: 1em 0;
        background-color: #f5f5f5;
    }
    .sql-result {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1em;
        margin: 1em 0;
        border-left: 4px solid #FF4B2B;
    }
    .status-message {
        padding: 1em;
        border-radius: 10px;
        margin: 1em 0;
    }
    .success-message {
        background-color: #d4edda;
        color: #155724;
    }
    .error-message {
        background-color: #f8d7da;
        color: #721c24;
    }
    /* Dark mode adjustments */
    @media (prefers-color-scheme: dark) {
        .chat-container {
            background-color: #2b2b2b;
        }
        .sql-result {
            background-color: #1e1e1e;
        }
    }
    </style>
"""
```

`knowledge/constructors_championship.json`

**サイズ**: 957.0 B | **行数**: 31 行
```json
{
    "table_name": "constructors_championship",
    "table_description": "Contains data for the constructor's championship from 1958 to 2020, capturing championship positions from when it was introduced.",
    "table_columns": [
      {
          "name": "index",
          "type": "int",
          "description": "Index of the row."
      },
      {
          "name": "year",
          "type": "int",
          "description": "Year of the championship."
      },
      {
          "name": "position",
          "type": "int",
          "description": "Final standing position of the team in the championship. Use position = 1 to get the champion team."
      },
      {
          "name": "team",
          "type": "text",
          "description": "Name of the Formula 1 team."
      },
      {
          "name": "points",
          "type": "int",
          "description": "Total points accumulated by the team during the championship year."
      }
  ]
}
```

`knowledge/drivers_championship.json`

**サイズ**: 1.3 KB | **行数**: 46 行
```json
{
    "table_name": "drivers_championship",
    "table_description": "Contains data for driver's championship standings from 1950-2020, detailing driver positions, teams, and points.",
    "table_columns": [
        {
            "name": "index",
            "type": "int",
            "description": "Index number of the record."
        },
        {
            "name": "year",
            "type": "int",
            "description": "The year of the championship."
        },
        {
            "name": "position",
            "type": "text",
            "description": "Final position of the driver in the championship."
        },
        {
            "name": "name",
            "type": "text",
            "description": "Full name of the driver."
        },
        {
            "name": "driver_tag",
            "type": "text",
            "description": "Abbreviated tag of the driver."
        },
        {
            "name": "nationality",
            "type": "text",
            "description": "Nationality of the driver."
        },
        {
            "name": "team",
            "type": "text",
            "description": "Racing team of the driver."
        },
        {
            "name": "points",
            "type": "float",
            "description": "Total points accumulated by the driver that season."
        }
    ]
}
```

`knowledge/fastest_laps.json`

**サイズ**: 1.0 KB | **行数**: 41 行
```json
{
    "table_name": "fastest_laps",
    "table_description": "Contains data for the fastest laps recorded in races from 1950-2020, including driver and team details.",
    "table_columns": [
      {
          "name": "index",
          "type": "int",
          "description": "Unique index for each entry."
      },
      {
          "name": "year",
          "type": "int",
          "description": "Year of the race."
      },
      {
          "name": "venue",
          "type": "text",
          "description": "Name of the race venue."
      },
      {
          "name": "name",
          "type": "text",
          "description": "Name of the driver."
      },
      {
          "name": "driver_tag",
          "type": "text",
          "description": "Abbreviated tag of the driver's name."
      },
      {
          "name": "team",
          "type": "text",
          "description": "Name of the racing team."
      },
      {
          "name": "lap_time",
          "type": "text",
          "description": "Fastest lap time recorded."
      }
    ]
}
```

`knowledge/race_results.json`

**サイズ**: 1.7 KB | **行数**: 61 行
```json
{
    "table_name": "race_results",
    "table_description": "Holds comprehensive race data for each Formula 1 race from 1950-2020, including positions, drivers, teams, and points.",
    "table_columns": [
        {
            "name": "index",
            "type": "int",
            "description": "Unique index for each entry."
        },
        {
            "name": "year",
            "type": "int",
            "description": "The year of the race."
        },
        {
            "name": "position",
            "type": "text",
            "description": "The finishing position of the driver."
        },
        {
            "name": "driver_no",
            "type": "int",
            "description": "Driver number."
        },
        {
            "name": "venue",
            "type": "text",
            "description": "Location of the race."
        },
        {
            "name": "name",
            "type": "text",
            "description": "Name of the driver."
        },
        {
            "name": "name_tag",
            "type": "text",
            "description": "Abbreviated tag of the driver's name."
        },
        {
            "name": "team",
            "type": "text",
            "description": "The racing team of the driver."
        },
        {
            "name": "laps",
            "type": "float",
            "description": "Number of laps completed."
        },
        {
            "name": "time",
            "type": "text",
            "description": "Finishing time or gap to the leader."
        },
        {
            "name": "points",
            "type": "float",
            "description": "Points earned in the race."
        }
    ]
}
```

`knowledge/race_wins.json`

**サイズ**: 1.3 KB | **行数**: 47 行
```json
{
    "table_name": "race_wins",
    "table_description": "Documents race win data from 1950-2020, detailing venue, winner, team, and race duration.",
    "table_columns": [
      {
          "name": "index",
          "type": "int",
          "description": "Unique index for each entry."
      },
      {
          "name": "venue",
          "type": "text",
          "description": "Venue where the race was held."
      },
      {
          "name": "date",
          "type": "text",
          "description": "Date of the race in the format 'DD Mon YYYY'.",
          "tip": "Use the `TO_DATE` function to convert the date to a date type."
      },
      {
          "name": "name",
          "type": "text",
          "description": "Name of the winning driver."
      },
      {
          "name": "name_tag",
          "type": "text",
          "description": "Tag associated with the driver's name."
      },
      {
          "name": "team",
          "type": "text",
          "description": "Team of the winning driver."
      },
      {
          "name": "laps",
          "type": "float",
          "description": "Number of laps completed in the race."
      },
      {
          "name": "time",
          "type": "text",
          "description": "Winning time of the race."
      }
  ]
}
```

`knowledge/sample_queries.sql`

**サイズ**: 1.5 KB | **行数**: 69 行
```sql
-- Here are some sample queries for reference

-- <query description>
-- How many races did the championship winners win each year?
-- </query description>
-- <query>
SELECT
    dc.year,
    dc.name AS champion_name,
    COUNT(rw.name) AS race_wins
FROM
    drivers_championship dc
JOIN
    race_wins rw
ON
    dc.name = rw.name AND dc.year = EXTRACT(YEAR FROM TO_DATE(rw.date, 'DD Mon YYYY'))
WHERE
    dc.position = '1'
GROUP BY
    dc.year, dc.name
ORDER BY
    dc.year;
-- </query>


-- <query description>
-- Compare the number of race wins vs championship positions for constructors in 2019
-- </query description>
-- <query>
WITH race_wins_2019 AS (
    SELECT team, COUNT(*) AS wins
    FROM race_wins
    WHERE EXTRACT(YEAR FROM TO_DATE(date, 'DD Mon YYYY')) = 2019
    GROUP BY team
),
constructors_positions_2019 AS (
    SELECT team, position
    FROM constructors_championship
    WHERE year = 2019
)

SELECT cp.team, cp.position, COALESCE(rw.wins, 0) AS wins
FROM constructors_positions_2019 cp
LEFT JOIN race_wins_2019 rw ON cp.team = rw.team
ORDER BY cp.position;
-- </query>

-- <query description>
-- Most race wins by a driver
-- </query description>
-- <query>
SELECT name, COUNT(*) AS win_count
FROM race_wins
GROUP BY name
ORDER BY win_count DESC
LIMIT 1;
-- </query>

-- <query description>
-- Which team won the most Constructors Championships?
-- </query description>
-- <query>
SELECT team, COUNT(*) AS championship_wins
FROM constructors_championship
WHERE position = 1
GROUP BY team
ORDER BY championship_wins DESC
LIMIT 1;
-- </query>
```


</Repository information>

</Input information>

上記の情報のみを使用してリリースノートを作成してください。
不明な点や情報が不足している部分については、推測せずにその旨を明記してください。
各項目の確信度を 🟢、🟡、🔴 で示し、提供された情報に直接基づいている場合は 🟢、やや推測を含む場合は 🟡、大きく推測している場合は 🔴 としてください。
前回のリリースノートに含まれる内容と重複する項目には 🔄 を付けてください。

        