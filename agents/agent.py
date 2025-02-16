"""SQL Agent implementation for F1 data analysis."""

from pathlib import Path
from textwrap import dedent
from typing import Optional
import os

from agno.agent import Agent
from agno.models.google import Gemini
from agno.models.openai import OpenAIChat
from agno.tools.file import FileTools
from agno.tools.sql import SQLTools

from .config import DB_URL, OUTPUT_DIR
from .knowledge import agent_knowledge, agent_storage
from .semantic_model import semantic_model_str

def load_prompt(filename: str) -> str:
    """Load prompt content from a markdown file.
    
    Args:
        filename: The name of the markdown file without extension
        
    Returns:
        The content of the markdown file as a string
    """
    prompt_dir = Path(__file__).parent / "prompts"
    prompt_path = prompt_dir / f"{filename}.md"
    return prompt_path.read_text(encoding="utf-8")


def get_sql_agent(
    user_id: Optional[str] = None,
    model_id: str = "openai:gpt-4",
    session_id: Optional[str] = None,
    debug_mode: bool = True,
) -> Agent:
    """Returns an instance of the SQL Agent.

    Args:
        user_id: Optional user identifier
        model_id: Model identifier in format 'provider:model_name'
        session_id: Optional session identifier
        debug_mode: Enable debug logging
    """
    # Parse model provider and name
    provider, model_name = model_id.split(":")

    # Select appropriate model class based on provider
    if provider == "openai":
        model = OpenAIChat(id=model_name)
    elif provider == "litellm":
        model = OpenAIChat(
            id=model_name,
            base_url=os.getenv("LITELLM_BASE_URL"),
            api_key=os.getenv("LITELLM_API_KEY"),
            metadata={"user_id": "demo_user",
                      "trace_user_id": "demo_trace_user"},
        )
    elif provider == "google":
        model = Gemini(id=model_name)
    else:
        raise ValueError(f"Unsupported model provider: {provider}")

    # Load prompts from markdown files
    description = load_prompt("description")
    instructions = load_prompt("instructions")
    rules = load_prompt("rules")

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
        tools=[SQLTools(db_url=DB_URL), FileTools(base_dir=OUTPUT_DIR)],
        add_history_to_messages=True,
        num_history_responses=3,
        debug_mode=debug_mode,
        description=dedent(description),
        instructions=dedent(f"""\
        {instructions}

        最後に、必ず従わなければならないルールのセットを以下に示します：
        <rules>
        {rules}
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
