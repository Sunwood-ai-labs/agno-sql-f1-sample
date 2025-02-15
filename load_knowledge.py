"""Load knowledge base for F1 SQL analysis."""

from agents.knowledge import agent_knowledge
from agno.utils.log import logger

def load_knowledge(recreate: bool = True):
    """Load SQL agent knowledge base.
    
    Args:
        recreate: If True, recreate the knowledge base. Otherwise, use existing if available.
    """
    logger.info("Loading SQL agent knowledge.")
    agent_knowledge.load(recreate=recreate)
    logger.info("SQL agent knowledge loaded.")

if __name__ == "__main__":
    load_knowledge()
