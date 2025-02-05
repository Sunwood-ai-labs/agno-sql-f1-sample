# Git Diff レポート

## バージョン比較

**v1.0.5** と **v1.0.6** の比較

## 差分の詳細

### .gitignore

```diff
index 1419ffaf..549ccfad 100644
--- a/.gitignore
+++ b/.gitignore
@@ -15,7 +15,6 @@
 # Machine specific
 .idea
 .vscode
-*.code-workspace
 
 # Ignore .env files
 .env
```

### agno.code-workspace

```diff
new file mode 100644
index 00000000..1e3fd025
--- /dev/null
+++ b/agno.code-workspace
@@ -0,0 +1,15 @@
+{
+	"folders": [
+		{
+			"path": "."
+		}
+	],
+	"settings": {
+    "python.analysis.extraPaths": [
+      "libs/agno",
+      "libs/infra/agno_docker",
+      "libs/infra/agno_aws"
+  ]
+  }
+}
+
```

### cookbook/agent_concepts/knowledge/readers/url_reader.py

```diff
new file mode 100644
index 00000000..0df31503
--- /dev/null
+++ b/cookbook/agent_concepts/knowledge/readers/url_reader.py
@@ -0,0 +1,21 @@
+from agno.document.chunking.recursive import RecursiveChunking
+from agno.document.reader.url_reader import URLReader
+
+reader = URLReader(chunking_strategy=RecursiveChunking(chunk_size=1000))
+
+try:
+    print("Starting read...")
+    documents = reader.read("https://docs.agno.com/llms-full.txt")
+
+    if documents:
+        for doc in documents:
+            print(doc.name)
+            print(doc.content)
+            print(f"Content length: {len(doc.content)}")
+            print("-" * 80)
+    else:
+        print("No documents were returned")
+
+except Exception as e:
+    print(f"Error type: {type(e)}")
+    print(f"Error occurred: {str(e)}")
```

### cookbook/agent_concepts/memory/09_using_other_models_for_memory.py

```diff
new file mode 100644
index 00000000..e2ee8625
--- /dev/null
+++ b/cookbook/agent_concepts/memory/09_using_other_models_for_memory.py
@@ -0,0 +1,226 @@
+"""🎓 StudyScout - Your AI-Powered Learning Companion!
+
+This advanced example shows how to create a sophisticated educational assistant
+that leverages multiple AI models for enhanced memory and personalized learning.
+The agent combines long-term memory, intelligent classification, and dynamic
+summarization to deliver an adaptive learning experience that grows with the user.
+
+Key Features:
+- Personalized learning paths based on user interests and goals
+- Long-term memory to track progress and preferences
+- Intelligent content curation from multiple sources
+- Interactive quizzes and assessments
+- Resource recommendations (articles, videos, courses)
+
+Example prompts to try:
+- "Create a 3-month learning path for becoming a full-stack developer"
+- "Explain quantum computing using gaming analogies based on my interests"
+- "Quiz me on world history, focusing on the Renaissance period"
+- "Find advanced machine learning resources matching my current skill level"
+- "Help me prepare for the AWS Solutions Architect certification"
+
+Run: `pip install groq agno` to install the dependencies
+"""
+
+from textwrap import dedent
+from typing import List, Optional
+
+import typer
+from agno.agent import Agent, AgentMemory
+from agno.memory.classifier import MemoryClassifier
+from agno.memory.db.sqlite import SqliteMemoryDb
+from agno.memory.manager import MemoryManager
+from agno.memory.summarizer import MemorySummarizer
+from agno.models.groq import Groq
+from agno.storage.agent.sqlite import SqliteAgentStorage
+from agno.tools.duckduckgo import DuckDuckGoTools
+from agno.tools.youtube import YouTubeTools
+from rich import print
+
+# Initialize storage components
+agent_storage = SqliteAgentStorage(table_name="study_sessions", db_file="tmp/agents.db")
+memory_db = SqliteMemoryDb(
+    table_name="study_memory",
+    db_file="tmp/agent_memory.db",
+)
+
+
+def study_agent(
+    user_id: Optional[str] = typer.Argument(None, help="User ID for the study session"),
+):
+    """
+    Initialize and run the StudyScout agent with the specified user ID.
+    If no user ID is provided, prompt for one.
+    """
+    # Get user ID if not provided as argument
+    if user_id is None:
+        user_id = typer.prompt("Enter your user ID", default="default_user")
+
+    session_id: Optional[str] = None
+
+    # Ask the user if they want to start a new session or continue an existing one
+    new = typer.confirm("Do you want to start a new study session?")
+
+    if not new:
+        existing_sessions: List[str] = agent_storage.get_all_session_ids(user_id)
+        if len(existing_sessions) > 0:
+            print("\nExisting sessions:")
+            for i, session in enumerate(existing_sessions, 1):
+                print(f"{i}. {session}")
+            session_idx = typer.prompt(
+                "Choose a session number to continue (or press Enter for most recent)",
+                default=1,
+            )
+            try:
+                session_id = existing_sessions[int(session_idx) - 1]
+            except (ValueError, IndexError):
+                session_id = existing_sessions[0]
+        else:
+            print("No existing sessions found. Starting a new session.")
+
+    agent = Agent(
+        name="StudyScout",
+        user_id=user_id,
+        session_id=session_id,
+        model=Groq(id="llama-3.3-70b-versatile"),
+        memory=AgentMemory(
+            db=memory_db,
+            create_user_memories=True,
+            update_user_memories_after_run=True,
+            classifier=MemoryClassifier(
+                model=Groq(id="llama-3.3-70b-versatile"),
+            ),
+            summarizer=MemorySummarizer(
+                model=Groq(id="llama-3.3-70b-versatile"),
+            ),
+            manager=MemoryManager(
+                model=Groq(id="llama-3.3-70b-versatile"),
+                db=memory_db,
+                user_id=user_id,
+            ),
+        ),
+        storage=agent_storage,
+        tools=[DuckDuckGoTools(), YouTubeTools()],
+        description=dedent("""\
+        You are StudyScout, an expert educational mentor with deep expertise in personalized learning! 📚
+
+        Your mission is to be an engaging, adaptive learning companion that helps users achieve their
+        educational goals through personalized guidance, interactive learning, and comprehensive resource curation.
+        """),
+        instructions=dedent("""\
+        Follow these steps for an optimal learning experience:
+
+        1. Initial Assessment
+        - Learn about the user's background, goals, and interests
+        - Assess current knowledge level
+        - Identify preferred learning styles
+
+        2. Learning Path Creation
+        - Design customized study plans, use DuckDuckGo to find resources
+        - Set clear milestones and objectives
+        - Adapt to user's pace and schedule
+
+        3. Content Delivery
+        - Break down complex topics into digestible chunks
+        - Use relevant analogies and examples
+        - Connect concepts to user's interests
+        - Provide multi-format resources (text, video, interactive)
+
+        4. Resource Curation
+        - Find relevant learning materials using DuckDuckGo
+        - Recommend quality educational content
+        - Share community learning opportunities
+        - Suggest practical exercises
+
+        Your teaching style:
+        - Be encouraging and supportive
+        - Use emojis for engagement (📚 ✨ 🎯)
+        - Incorporate interactive elements
+        - Provide clear explanations
+        - Use memory to personalize interactions
+        - Adapt to learning preferences
+        - Include progress celebrations
+        - Offer study technique tips
+
+        Remember to:
+        - Keep sessions focused and structured
+        - Provide regular encouragement
+        - Celebrate learning milestones
+        - Address learning obstacles
+        - Maintain learning continuity\
+        """),
+        additional_context=dedent(f"""\
+        - User ID: {user_id}
+        - Session Type: {"New Session" if session_id is None else "Continuing Session"}
+        - Available Tools: Web Search, YouTube Resources
+        - Memory System: Active
+        """),
+        add_history_to_messages=True,
+        num_history_responses=3,
+        show_tool_calls=True,
+        read_chat_history=True,
+        markdown=True,
+    )
+
+    print("\n📚 Welcome to StudyScout - Your Personal Learning Companion! 🎓")
+    if session_id is None:
+        session_id = agent.session_id
+        if session_id is not None:
+            print(f"[bold green]Started New Study Session: {session_id}[/bold green]\n")
+        else:
+            print("[bold green]Started New Study Session[/bold green]\n")
+    else:
+        print(f"[bold blue]Continuing Previous Session: {session_id}[/bold blue]\n")
+
+    # Runs the agent as a command line application
+    agent.cli_app(markdown=True, stream=True)
+
+
+if __name__ == "__main__":
+    typer.run(study_agent)
+
+"""
+Example Usage:
+
+1. Start a new learning session:
+   ```bash
+   python 03_using_other_models_for_memory.py
+   ```
+
+2. Continue with specific user ID:
+   ```bash
+   python 03_using_other_models_for_memory.py "learner_123"
+   ```
+
+Advanced Learning Scenarios:
+
+Technical Skills:
+1. "Guide me through learning system design principles"
+2. "Help me master Python data structures and algorithms"
+3. "Create a DevOps learning pathway for beginners"
+4. "Teach me about cloud architecture patterns"
+
+Academic Subjects:
+1. "Explain organic chemistry reactions using cooking analogies"
+2. "Help me understand advanced statistics concepts"
+3. "Break down quantum mechanics principles"
+4. "Guide me through macroeconomics theories"
+
+Professional Development:
+1. "Prepare me for product management interviews"
+2. "Create a data science portfolio development plan"
+3. "Design a public speaking improvement program"
+4. "Build a cybersecurity certification roadmap"
+
+Language Learning:
+1. "Create an immersive Japanese learning experience"
+2. "Help me practice business English scenarios"
+3. "Design a Spanish conversation practice routine"
+4. "Prepare me for the IELTS academic test"
+
+Creative Skills:
+1. "Guide me through digital art fundamentals"
+2. "Help me develop creative writing techniques"
+3. "Create a music theory learning progression"
+4. "Design a UI/UX design learning path"
+"""
```

### cookbook/examples/agents/deep_knowledge.py

```diff
new file mode 100644
index 00000000..0abc3468
--- /dev/null
+++ b/cookbook/examples/agents/deep_knowledge.py
@@ -0,0 +1,220 @@
+"""🤔 DeepKnowledge - An AI Agent that iteratively searches a knowledge base to answer questions
+
+This agent performs iterative searches through its knowledge base, breaking down complex
+queries into sub-questions, and synthesizing comprehensive answers. It's designed to explore
+topics deeply and thoroughly by following chains of reasoning.
+
+In this example, the agent uses the Agno documentation as a knowledge base
+
+Key Features:
+- Iteratively searches a knowledge base
+- Source attribution and citations
+
+Run `pip install openai lancedb tantivy inquirer agno` to install dependencies.
+"""
+
+from textwrap import dedent
+from typing import List, Optional
+
+import inquirer
+import typer
+from agno.agent import Agent
+from agno.embedder.openai import OpenAIEmbedder
+from agno.knowledge.url import UrlKnowledge
+from agno.models.openai import OpenAIChat
+from agno.storage.agent.sqlite import SqliteAgentStorage
+from agno.vectordb.lancedb import LanceDb, SearchType
+from rich import print
+
+
+def initialize_knowledge_base():
+    """Initialize the knowledge base with your preferred documentation or knowledge source
+    Here we use Agno docs as an example, but you can replace with any relevant URLs
+    """
+    agent_knowledge = UrlKnowledge(
+        urls=["https://docs.agno.com/llms-full.txt"],
+        vector_db=LanceDb(
+            uri="tmp/lancedb",
+            table_name="deep_knowledge_knowledge",
+            search_type=SearchType.hybrid,
+            embedder=OpenAIEmbedder(id="text-embedding-3-small"),
+        ),
+    )
+    # Load the knowledge base (comment out after first run)
+    # agent_knowledge.load()
+    return agent_knowledge
+
+
+def get_agent_storage():
+    """Return agent storage"""
+    return SqliteAgentStorage(
+        table_name="deep_knowledge_sessions", db_file="tmp/agents.db"
+    )
+
+
+def create_agent(session_id: Optional[str] = None) -> Agent:
+    """Create and return a configured DeepKnowledge agent."""
+    agent_knowledge = initialize_knowledge_base()
+    agent_storage = get_agent_storage()
+    return Agent(
+        name="DeepKnowledge",
+        session_id=session_id,
+        model=OpenAIChat(id="gpt-4o"),
+        description=dedent("""\
+        You are DeepKnowledge, an advanced reasoning agent designed to provide thorough,
+        well-researched answers to any query by searching your knowledge base.
+
+        Your strengths include:
+        - Breaking down complex topics into manageable components
+        - Connecting information across multiple domains
+        - Providing nuanced, well-researched answers
+        - Maintaining intellectual honesty and citing sources
+        - Explaining complex concepts in clear, accessible terms"""),
+        instructions=dedent("""\
+        Your mission is to leave no stone unturned in your pursuit of the correct answer.
+
+        To achieve this, follow these steps:
+        1. **Analyze the input and break it down into key components**.
+        2. **Search terms**: You must identify at least 3-5 key search terms to search for.
+        3. **Initial Search:** Searching your knowledge base for relevant information. You must make atleast 3 searches to get all relevant information.
+        4. **Evaluation:** If the answer from the knowledge base is incomplete, ambiguous, or insufficient - Ask the user for clarification. Do not make informed guesses.
+        5. **Iterative Process:**
+            - Continue searching your knowledge base till you have a comprehensive answer.
+            - Reevaluate the completeness of your answer after each search iteration.
+            - Repeat the search process until you are confident that every aspect of the question is addressed.
+        4. **Reasoning Documentation:** Clearly document your reasoning process:
+            - Note when additional searches were triggered.
+            - Indicate which pieces of information came from the knowledge base and where it was sourced from.
+            - Explain how you reconciled any conflicting or ambiguous information.
+        5. **Final Synthesis:** Only finalize and present your answer once you have verified it through multiple search passes.
+            Include all pertinent details and provide proper references.
+        6. **Continuous Improvement:** If new, relevant information emerges even after presenting your answer,
+            be prepared to update or expand upon your response.
+
+        **Communication Style:**
+        - Use clear and concise language.
+        - Organize your response with numbered steps, bullet points, or short paragraphs as needed.
+        - Be transparent about your search process and cite your sources.
+        - Ensure that your final answer is comprehensive and leaves no part of the query unaddressed.
+
+        Remember: **Do not finalize your answer until every angle of the question has been explored.**"""),
+        additional_context=dedent("""\
+        You should only respond with the final answer and the reasoning process.
+        No need to include irrelevant information.
+
+        - User ID: {user_id}
+        - Memory: You have access to your previous search results and reasoning process.
+        """),
+        knowledge=agent_knowledge,
+        storage=agent_storage,
+        add_history_to_messages=True,
+        num_history_responses=3,
+        show_tool_calls=True,
+        read_chat_history=True,
+        markdown=True,
+    )
+
+
+def get_example_topics() -> List[str]:
+    """Return a list of example topics for the agent."""
+    return [
+        "What are AI agents and how do they work in Agno?",
+        "What chunking strategies does Agno support for text processing?",
+        "How can I implement custom tools in Agno?",
+        "How does knowledge retrieval work in Agno?",
+        "What types of embeddings does Agno support?",
+    ]
+
+
+def handle_session_selection() -> Optional[str]:
+    """Handle session selection and return the selected session ID."""
+    agent_storage = get_agent_storage()
+
+    new = typer.confirm("Do you want to start a new session?", default=True)
+    if new:
+        return None
+
+    existing_sessions: List[str] = agent_storage.get_all_session_ids()
+    if not existing_sessions:
+        print("No existing sessions found. Starting a new session.")
+        return None
+
+    print("\nExisting sessions:")
+    for i, session in enumerate(existing_sessions, 1):
+        print(f"{i}. {session}")
+
+    session_idx = typer.prompt(
+        "Choose a session number to continue (or press Enter for most recent)",
+        default=1,
+    )
+
+    try:
+        return existing_sessions[int(session_idx) - 1]
+    except (ValueError, IndexError):
+        return existing_sessions[0]
+
+
+def run_interactive_loop(agent: Agent):
+    """Run the interactive question-answering loop."""
+    example_topics = get_example_topics()
+
+    while True:
+        choices = [f"{i + 1}. {topic}" for i, topic in enumerate(example_topics)]
+        choices.extend(["Enter custom question...", "Exit"])
+
+        questions = [
+            inquirer.List(
+                "topic",
+                message="Select a topic or ask a different question:",
+                choices=choices,
+            )
+        ]
+        answer = inquirer.prompt(questions)
+
+        if answer["topic"] == "Exit":
+            break
+
+        if answer["topic"] == "Enter custom question...":
+            questions = [inquirer.Text("custom", message="Enter your question:")]
+            custom_answer = inquirer.prompt(questions)
+            topic = custom_answer["custom"]
+        else:
+            topic = example_topics[int(answer["topic"].split(".")[0]) - 1]
+
+        agent.print_response(topic, stream=True)
+
+
+def deep_knowledge_agent():
+    """Main function to run the DeepKnowledge agent."""
+
+    session_id = handle_session_selection()
+    agent = create_agent(session_id)
+
+    print("\n🤔 Welcome to DeepKnowledge - Your Advanced Research Assistant! 📚")
+    if session_id is None:
+        session_id = agent.session_id
+        if session_id is not None:
+            print(f"[bold green]Started New Session: {session_id}[/bold green]\n")
+        else:
+            print("[bold green]Started New Session[/bold green]\n")
+    else:
+        print(f"[bold blue]Continuing Previous Session: {session_id}[/bold blue]\n")
+
+    run_interactive_loop(agent)
+
+
+if __name__ == "__main__":
+    typer.run(deep_knowledge_agent)
+
+# Example prompts to try:
+"""
+Explore Agno's capabilities with these queries:
+1. "What are the different types of agents in Agno?"
+2. "How does Agno handle knowledge base management?"
+3. "What embedding models does Agno support?"
+4. "How can I implement custom tools in Agno?"
+5. "What storage options are available for workflow caching?"
+6. "How does Agno handle streaming responses?"
+7. "What types of LLM providers does Agno support?"
+8. "How can I implement custom knowledge sources?"
+"""
```

### cookbook/tools/github_tools.py

```diff
index 6a3010d0..8cd39be5 100644
--- a/cookbook/tools/github_tools.py
+++ b/cookbook/tools/github_tools.py
@@ -11,13 +11,23 @@ agent = Agent(
 )
 agent.print_response("List open pull requests", markdown=True)
 
+# # Example usage: Search for python projects on github that have more than 1000 stars
+# agent.print_response("Search for python projects on github that have more than 1000 stars", markdown=True, stream=True)
+
+# # Example usage: Search for python projects on github that have more than 1000 stars, but return the 2nd page of results
+# agent.print_response("Search for python projects on github that have more than 1000 stars, but return the 2nd page of results", markdown=True, stream=True)
+
 # # Example usage: Get pull request details
 # agent.print_response("Get details of #1239", markdown=True)
+
 # # Example usage: Get pull request changes
 # agent.print_response("Show changes for #1239", markdown=True)
+
 # # Example usage: List open issues
 # agent.print_response("What is the latest opened issue?", markdown=True)
+
 # # Example usage: Create an issue
 # agent.print_response("Explain the comments for the most recent issue", markdown=True)
+
 # # Example usage: Create a Repo
 # agent.print_response("Create a repo called agno-test and add description hello", markdown=True)
```

### cookbook/tools/google_maps_tools.py

```diff
new file mode 100644
index 00000000..d949f123
--- /dev/null
+++ b/cookbook/tools/google_maps_tools.py
@@ -0,0 +1,143 @@
+"""
+Business Contact Search Agent for finding and extracting business contact information.
+This example demonstrates various Google Maps API functionalities including business search,
+directions, geocoding, address validation, and more.
+
+Prerequisites:
+- Set the environment variable `GOOGLE_MAPS_API_KEY` with your Google Maps API key.
+  You can obtain the API key from the Google Cloud Console:
+  https://console.cloud.google.com/projectselector2/google/maps-apis/credentials
+
+- You also need to activate the Address Validation API for your .
+  https://console.developers.google.com/apis/api/addressvalidation.googleapis.com
+
+"""
+
+from agno.agent import Agent
+from agno.tools.crawl4ai import Crawl4aiTools
+from agno.tools.google_maps import GoogleMapTools
+
+agent = Agent(
+    name="Maps API Demo Agent",
+    tools=[
+        GoogleMapTools(),  # For  on Google Maps
+        Crawl4aiTools(max_length=5000),  # For scraping business websites
+    ],
+    description="You are a location and business information specialist that can help with various mapping and location-based queries.",
+    instructions=[
+        "When given a search query:",
+        "1. Use appropriate Google Maps methods based on the query type",
+        "2. For place searches, combine Maps data with website data when available",
+        "3. Format responses clearly and provide relevant details based on the query",
+        "4. Handle errors gracefully and provide meaningful feedback",
+    ],
+    markdown=True,
+    show_tool_calls=True,
+)
+
+# Example 1: Business Search
+print("\n=== Business Search Example ===")
+agent.print_response(
+    "Find me highly rated Indian restaurants in Phoenix, AZ with their contact details",
+    markdown=True,
+    stream=True,
+)
+
+# Example 2: Directions
+print("\n=== Directions Example ===")
+agent.print_response(
+    """Get driving directions from 'Phoenix Sky Harbor Airport' to 'Desert Botanical Garden', 
+    avoiding highways if possible""",
+    markdown=True,
+    stream=True,
+)
+
+# Example 3: Address Validation and Geocoding
+print("\n=== Address Validation and Geocoding Example ===")
+agent.print_response(
+    """Please validate and geocode this address: 
+    '1600 Amphitheatre Parkway, Mountain View, CA'""",
+    markdown=True,
+    stream=True,
+)
+
+# Example 4: Distance Matrix
+print("\n=== Distance Matrix Example ===")
+agent.print_response(
+    """Calculate the travel time and distance between these locations in Phoenix:
+    Origins: ['Phoenix Sky Harbor Airport', 'Downtown Phoenix']
+    Destinations: ['Desert Botanical Garden', 'Phoenix Zoo']""",
+    markdown=True,
+    stream=True,
+)
+
+# Example 5: Nearby Places and Details
+print("\n=== Nearby Places Example ===")
+agent.print_response(
+    """Find coffee shops near Arizona State University Tempe campus. 
+    Include ratings and opening hours if available.""",
+    markdown=True,
+    stream=True,
+)
+
+# Example 6: Reverse Geocoding and Timezone
+print("\n=== Reverse Geocoding and Timezone Example ===")
+agent.print_response(
+    """Get the address and timezone information for these coordinates:
+    Latitude: 33.4484, Longitude: -112.0740 (Phoenix)""",
+    markdown=True,
+    stream=True,
+)
+
+# Example 7: Multi-step Route Planning
+print("\n=== Multi-step Route Planning Example ===")
+agent.print_response(
+    """Plan a route with multiple stops in Phoenix:
+    Start: Phoenix Sky Harbor Airport
+    Stops: 
+    1. Arizona Science Center
+    2. Heard Museum
+    3. Desert Botanical Garden
+    End: Return to Airport
+    Please include estimated travel times between each stop.""",
+    markdown=True,
+    stream=True,
+)
+
+# Example 8: Location Analysis
+print("\n=== Location Analysis Example ===")
+agent.print_response(
+    """Analyze this location in Phoenix:
+    Address: '2301 N Central Ave, Phoenix, AZ 85004'
+    Please provide:
+    1. Exact coordinates
+    2. Nearby landmarks
+    3. Elevation data
+    4. Local timezone""",
+    markdown=True,
+    stream=True,
+)
+
+# Example 9: Business Hours and Accessibility
+print("\n=== Business Hours and Accessibility Example ===")
+agent.print_response(
+    """Find museums in Phoenix that are:
+    1. Open on Mondays
+    2. Have wheelchair accessibility
+    3. Within 5 miles of downtown
+    Include their opening hours and contact information.""",
+    markdown=True,
+    stream=True,
+)
+
+# Example 10: Transit Options
+print("\n=== Transit Options Example ===")
+agent.print_response(
+    """Compare different travel modes from 'Phoenix Convention Center' to 'Phoenix Art Museum':
+    1. Driving
+    2. Walking
+    3. Transit (if available)
+    Include estimated time and distance for each option.""",
+    markdown=True,
+    stream=True,
+)
```

### cookbook/tools/zoom_tools.py

```diff
index 4fe0dc97..88e0f725 100644
--- a/cookbook/tools/zoom_tools.py
+++ b/cookbook/tools/zoom_tools.py
@@ -1,86 +1,60 @@
+"""
+Zoom Tools Example - Demonstrates how to use the Zoom toolkit for meeting management.
+
+This example shows how to:
+1. Set up authentication with Zoom API
+2. Initialize the ZoomTools with proper credentials
+3. Create an agent that can manage Zoom meetings
+4. Use various Zoom API functionalities through natural language
+
+Prerequisites:
+-------------
+1. Create a Server-to-Server OAuth app in Zoom Marketplace:
+   - Visit https://marketplace.zoom.us/
+   - Create a new app. Go to Develop -> Build App -> Server-to-Server OAuth.
+   - Add required scopes:
+     * meeting:write:admin
+     * meeting:read:admin
+     * cloud_recording:read:admin
+   - Copy Account ID, Client ID, and Client Secret
+
+2. Set environment variables:
+   export ZOOM_ACCOUNT_ID=your_account_id
+   export ZOOM_CLIENT_ID=your_client_id
+   export ZOOM_CLIENT_SECRET=your_client_secret
+
+Features:
+---------
+- Schedule new meetings
+- Get meeting details
+- List all meetings
+- Get upcoming meetings
+- Delete meetings
+- Get meeting recordings
+
+Usage:
+------
+Run this script with proper environment variables set to interact with
+the Zoom API through natural language commands.
+"""
+
 import os
-import time
-from typing import Optional
 
-import requests
 from agno.agent import Agent
 from agno.models.openai import OpenAIChat
 from agno.tools.zoom import ZoomTools
-from agno.utils.log import logger
 
 # Get environment variables
 ACCOUNT_ID = os.getenv("ZOOM_ACCOUNT_ID")
 CLIENT_ID = os.getenv("ZOOM_CLIENT_ID")
 CLIENT_SECRET = os.getenv("ZOOM_CLIENT_SECRET")
 
-
-class CustomZoomTools(ZoomTools):
-    def __init__(
-        self,
-        account_id: Optional[str] = None,
-        client_id: Optional[str] = None,
-        client_secret: Optional[str] = None,
-        name: str = "zoom_tool",
-    ):
-        super().__init__(
-            account_id=account_id,
-            client_id=client_id,
-            client_secret=client_secret,
-            name=name,
-        )
-        self.token_url = "https://zoom.us/oauth/token"
-        self.access_token = None
-        self.token_expires_at = 0
-
-    def get_access_token(self) -> str:
-        """
-        Obtain or refresh the access token for Zoom API.
-
-        to get the  account_id  ,client_id  ,client_secret
-        https://developers.zoom.us/docs/internal-apps/create/
-
-        for oauth 2.0
-        https://developers.zoom.us/docs/integrations/oauth/
-        Returns:
-            A string containing the access token or an empty string if token retrieval fails.
-        """
-        if self.access_token and time.time() < self.token_expires_at:
-            return str(self.access_token)
-
-        headers = {"Content-Type": "application/x-www-form-urlencoded"}
-        data = {"grant_type": "account_credentials", "account_id": self.account_id}
-
-        try:
-            response = requests.post(
-                self.token_url,
-                headers=headers,
-                data=data,
-                auth=(self.client_id, self.client_secret),
-            )
-            response.raise_for_status()
-
-            token_info = response.json()
-            self.access_token = token_info["access_token"]
-            expires_in = token_info["expires_in"]
-            self.token_expires_at = time.time() + expires_in - 60
-
-            self._set_parent_token(str(self.access_token))
-            return str(self.access_token)
-        except requests.RequestException as e:
-            logger.error(f"Error fetching access token: {e}")
-            return ""
-
-    def _set_parent_token(self, token: str) -> None:
-        """Helper method to set the token in the parent ZoomTool class"""
-        if token:
-            self._ZoomTool__access_token = token
-
-
-zoom_tools = CustomZoomTools(
+# Initialize Zoom tools with credentials
+zoom_tools = ZoomTools(
     account_id=ACCOUNT_ID, client_id=CLIENT_ID, client_secret=CLIENT_SECRET
 )
 
-
+# Create an agent with Zoom capabilities
 agent = Agent(
     name="Zoom Meeting Manager",
     agent_id="zoom-meeting-manager",
@@ -115,14 +89,15 @@ agent = Agent(
     ],
 )
 
-
+# Example usage - uncomment the ones you want to try
 agent.print_response(
-    "Schedule a meeting titled 'Team Sync' 10th december 2024 at 2 PM IST for 45 minutes"
+    "Schedule a meeting titled 'Team Sync' for tomorrow at 2 PM UTC for 45 minutes"
 )
-# agent.print_response("delete a meeting titled 'Team Sync' which scheduled tomorrow at 2 PM UTC for 45 minutes")
+
+# More examples (uncomment to use):
 # agent.print_response("What meetings do I have coming up?")
 # agent.print_response("List all my scheduled meetings")
 # agent.print_response("Get details for my most recent meeting")
-# agent.print_response("Get the recordings for my python automation meeting")
-# agent.print_response("Please delete all my scheduled meetings")
-# agent.print_response("Schedule 10 meetings titled 'Daily Standup' for the next 10 days at 5 PM UTC, each for 30 minutes")
+# agent.print_response("Get the recordings for my last team meeting")
+# agent.print_response("Delete the meeting titled 'Team Sync'")
+# agent.print_response("Schedule daily standup meetings for next week at 10 AM UTC")
```

### evals/performance/other/crewai_instantiation.py

```diff
index 088992ee..d1e3d4e7 100644
--- a/evals/performance/other/crewai_instantiation.py
+++ b/evals/performance/other/crewai_instantiation.py
@@ -1,12 +1,31 @@
-"""Run `pip install openai memory_profiler crewai` to install dependencies."""
+"""Run `pip install openai memory_profiler crewai crewai[tools]` to install dependencies."""
+from typing import Literal
 
 from crewai.agent import Agent
+from crewai.tools import tool
 from agno.eval.perf import PerfEval
 
+
+@tool("Tool Name")
+def get_weather(city: Literal["nyc", "sf"]):
+    """Use this to get weather information."""
+    if city == "nyc":
+        return "It might be cloudy in nyc"
+    elif city == "sf":
+        return "It's always sunny in sf"
+    else:
+        raise AssertionError("Unknown city")
+
+tools = [get_weather]
+
 def instantiate_agent():
-    return Agent(llm='gpt-4o', role='Test Agent', goal='Be concise, reply with one sentence.', backstory='Test')
+    return Agent(llm='gpt-4o',
+                 role='Test Agent',
+                 goal='Be concise, reply with one sentence.',
+                 tools=tools,
+                 backstory='Test')
 
-crew_instantiation = PerfEval(func=instantiate_agent, num_iterations=10)
+crew_instantiation = PerfEval(func=instantiate_agent, num_iterations=1000)
 
 if __name__ == "__main__":
     crew_instantiation.run(print_results=True)
```

### evals/performance/other/pydantic_ai_instantiation.py

```diff
index d6872391..85a6839b 100644
--- a/evals/performance/other/pydantic_ai_instantiation.py
+++ b/evals/performance/other/pydantic_ai_instantiation.py
@@ -1,10 +1,24 @@
 """Run `pip install openai pydantic-ai` to install dependencies."""
+from typing import Literal
 
 from pydantic_ai import Agent
 from agno.eval.perf import PerfEval
 
+
 def instantiate_agent():
-    return Agent('openai:gpt-4o', system_prompt='Be concise, reply with one sentence.')
+    agent =  Agent('openai:gpt-4o', system_prompt='Be concise, reply with one sentence.')
+
+    @agent.tool_plain
+    def get_weather(city: Literal["nyc", "sf"]):
+        """Use this to get weather information."""
+        if city == "nyc":
+            return "It might be cloudy in nyc"
+        elif city == "sf":
+            return "It's always sunny in sf"
+        else:
+            raise AssertionError("Unknown city")
+
+    return agent
 
 pydantic_instantiation = PerfEval(func=instantiate_agent, num_iterations=1000)
 
```

### evals/performance/other/smolagents_instantiation.py

```diff
index ca4cd307..ee9e4711 100644
--- a/evals/performance/other/smolagents_instantiation.py
+++ b/evals/performance/other/smolagents_instantiation.py
@@ -1,12 +1,37 @@
 """Run `pip install memory_profiler smolagents` to install dependencies."""
+from typing import Literal
 
 from agno.eval.perf import PerfEval
-from smolagents import ToolCallingAgent, HfApiModel
+from smolagents import ToolCallingAgent, HfApiModel, Tool
+
+
+class WeatherTool(Tool):
+    name = "weather_tool"
+    description = """
+    This is a tool that tells the weather"""
+    inputs = {
+        "city": {
+            "type": "string",
+            "description": "The city to look up",
+        }
+    }
+    output_type = "string"
+
+    def forward(self, city: str):
+        """Use this to get weather information."""
+        if city == "nyc":
+            return "It might be cloudy in nyc"
+        elif city == "sf":
+            return "It's always sunny in sf"
+        else:
+            raise AssertionError("Unknown city")
+
+
 
 def instantiate_agent():
-    return ToolCallingAgent(tools=[], model=HfApiModel(model_id="meta-llama/Llama-3.3-70B-Instruct"))
+    return ToolCallingAgent(tools=[WeatherTool()], model=HfApiModel(model_id="meta-llama/Llama-3.3-70B-Instruct"))
 
-smolagents_instantiation = PerfEval(func=instantiate_agent, num_iterations=10)
+smolagents_instantiation = PerfEval(func=instantiate_agent, num_iterations=1000)
 
 if __name__ == "__main__":
     smolagents_instantiation.run(print_results=True)
```

### libs/agno/agno/document/reader/url_reader.py

```diff
new file mode 100644
index 00000000..f8d02eb1
--- /dev/null
+++ b/libs/agno/agno/document/reader/url_reader.py
@@ -0,0 +1,52 @@
+from typing import List
+from urllib.parse import urlparse
+
+from agno.document.base import Document
+from agno.document.reader.base import Reader
+from agno.utils.log import logger
+
+
+class URLReader(Reader):
+    """Reader for general URL content"""
+
+    def read(self, url: str) -> List[Document]:
+        if not url:
+            raise ValueError("No url provided")
+
+        try:
+            import httpx
+        except ImportError:
+            raise ImportError("`httpx` not installed. Please install it via `pip install httpx`.")
+
+        logger.info(f"Reading: {url}")
+        response = httpx.get(url)
+
+        try:
+            logger.debug(f"Status: {response.status_code}")
+            logger.debug(f"Content size: {len(response.content)} bytes")
+        except Exception:
+            pass
+
+        try:
+            response.raise_for_status()
+        except httpx.HTTPStatusError as e:
+            logger.error(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
+            raise
+
+        # Create a clean document name from the URL
+        parsed_url = urlparse(url)
+        doc_name = parsed_url.path.strip("/").replace("/", "_").replace(" ", "_")
+        if not doc_name:
+            doc_name = parsed_url.netloc
+
+        # Create a single document with the URL content
+        document = Document(
+            name=doc_name,
+            id=doc_name,
+            meta_data={"url": url},
+            content=response.text,
+        )
+
+        if self.chunk:
+            return self.chunk_document(document)
+        return [document]
```

### libs/agno/agno/knowledge/url.py

```diff
new file mode 100644
index 00000000..59210241
--- /dev/null
+++ b/libs/agno/agno/knowledge/url.py
@@ -0,0 +1,26 @@
+from typing import Iterator, List
+
+from agno.document import Document
+from agno.document.reader.url_reader import URLReader
+from agno.knowledge.agent import AgentKnowledge
+from agno.utils.log import logger
+
+
+class UrlKnowledge(AgentKnowledge):
+    urls: List[str] = []
+    reader: URLReader = URLReader()
+
+    @property
+    def document_lists(self) -> Iterator[List[Document]]:
+        """Iterate over URLs and yield lists of documents.
+        Each object yielded by the iterator is a list of documents.
+
+        Returns:
+            Iterator[List[Document]]: Iterator yielding list of documents
+        """
+
+        for url in self.urls:
+            try:
+                yield self.reader.read(url=url)
+            except Exception as e:
+                logger.error(f"Error reading URL {url}: {str(e)}")
```

### libs/agno/agno/tools/github.py

```diff
index 113b0725..f2a2cca6 100644
--- a/libs/agno/agno/tools/github.py
+++ b/libs/agno/agno/tools/github.py
@@ -67,23 +67,32 @@ class GithubTools(Toolkit):
             logger.debug("Authenticating with public GitHub")
             return Github(auth=auth)
 
-    def search_repositories(self, query: str, sort: str = "stars", order: str = "desc", per_page: int = 5) -> str:
+    def search_repositories(
+        self, query: str, sort: str = "stars", order: str = "desc", page: int = 1, per_page: int = 30
+    ) -> str:
         """Search for repositories on GitHub.
 
         Args:
             query (str): The search query keywords.
             sort (str, optional): The field to sort results by. Can be 'stars', 'forks', or 'updated'. Defaults to 'stars'.
             order (str, optional): The order of results. Can be 'asc' or 'desc'. Defaults to 'desc'.
-            per_page (int, optional): Number of results per page. Defaults to 5.
+            page (int, optional): Page number of results to return, counting from 1. Defaults to 1.
+            per_page (int, optional): Number of results per page. Max 100. Defaults to 30.
+            Note: GitHub's Search API has a maximum limit of 1000 results per query.
 
         Returns:
             A JSON-formatted string containing a list of repositories matching the search query.
         """
-        logger.debug(f"Searching repositories with query: '{query}'")
+        logger.debug(f"Searching repositories with query: '{query}', page: {page}, per_page: {per_page}")
         try:
+            # Ensure per_page doesn't exceed GitHub's max of 100
+            per_page = min(per_page, 100)
+
             repositories = self.g.search_repositories(query=query, sort=sort, order=order)
+
+            # Get the specified page of results
             repo_list = []
-            for repo in repositories[:per_page]:
+            for repo in repositories.get_page(page - 1):
                 repo_info = {
                     "full_name": repo.full_name,
                     "description": repo.description,
@@ -93,7 +102,12 @@ class GithubTools(Toolkit):
                     "language": repo.language,
                 }
                 repo_list.append(repo_info)
+
+                if len(repo_list) >= per_page:
+                    break
+
             return json.dumps(repo_list, indent=2)
+
         except GithubException as e:
             logger.error(f"Error searching repositories: {e}")
             return json.dumps({"error": str(e)})
```

### libs/agno/agno/tools/google_maps.py

```diff
new file mode 100644
index 00000000..cad7fcef
--- /dev/null
+++ b/libs/agno/agno/tools/google_maps.py
@@ -0,0 +1,277 @@
+"""
+This module provides tools for searching business information using the Google Maps API.
+
+Prerequisites:
+- Set the environment variable `GOOGLE_MAPS_API_KEY` with your Google Maps API key.
+  You can obtain the API key from the Google Cloud Console:
+  https://console.cloud.google.com/projectselector2/google/maps-apis/credentials
+
+- You also need to activate the Address Validation API for your .
+  https://console.developers.google.com/apis/api/addressvalidation.googleapis.com
+
+"""
+
+import json
+from datetime import datetime
+from os import getenv
+from typing import List, Optional
+
+from agno.tools import Toolkit
+
+try:
+    import googlemaps
+except ImportError:
+    print("Error importing googlemaps. Please install the package using `pip install googlemaps`.")
+
+
+class GoogleMapTools(Toolkit):
+    def __init__(
+        self,
+        key: Optional[str] = None,
+        search_places: bool = True,
+        get_directions: bool = True,
+        validate_address: bool = True,
+        geocode_address: bool = True,
+        reverse_geocode: bool = True,
+        get_distance_matrix: bool = True,
+        get_elevation: bool = True,
+        get_timezone: bool = True,
+    ):
+        super().__init__(name="google_maps")
+
+        api_key = key or getenv("GOOGLE_MAPS_API_KEY")
+        if not api_key:
+            raise ValueError("GOOGLE_MAPS_API_KEY is not set in the environment variables.")
+        self.client = googlemaps.Client(key=api_key)
+
+        if search_places:
+            self.register(self.search_places)
+        if get_directions:
+            self.register(self.get_directions)
+        if validate_address:
+            self.register(self.validate_address)
+        if geocode_address:
+            self.register(self.geocode_address)
+        if reverse_geocode:
+            self.register(self.reverse_geocode)
+        if get_distance_matrix:
+            self.register(self.get_distance_matrix)
+        if get_elevation:
+            self.register(self.get_elevation)
+        if get_timezone:
+            self.register(self.get_timezone)
+
+    def search_places(self, query: str) -> str:
+        """
+        Search for places using Google Maps Places API.
+        This tool takes a search query and returns detailed place information.
+
+        Args:
+            query (str): The query string to search for using Google Maps Search API. (e.g., "dental clinics in Noida")
+
+        Returns:
+            Stringified list of dictionaries containing business information like name, address, phone, website, rating, and reviews etc.
+        """
+        try:
+            # Perform places search
+            places_result = self.client.places(query)
+
+            if not places_result or "results" not in places_result:
+                return str([])
+
+            places = []
+            for place in places_result["results"]:
+                place_info = {
+                    "name": place.get("name", ""),
+                    "address": place.get("formatted_address", ""),
+                    "rating": place.get("rating", 0.0),
+                    "reviews": place.get("user_ratings_total", 0),
+                    "place_id": place.get("place_id", ""),
+                }
+
+                # Get place details for additional information
+                if place_info.get("place_id"):
+                    try:
+                        details = self.client.place(place_info["place_id"])
+                        if details and "result" in details:
+                            result = details["result"]
+                            place_info.update(
+                                {
+                                    "phone": result.get("formatted_phone_number", ""),
+                                    "website": result.get("website", ""),
+                                    "hours": result.get("opening_hours", {}).get("weekday_text", []),
+                                }
+                            )
+                    except Exception as e:
+                        print(f"Error getting place details: {str(e)}")
+                        # Continue with basic place info if details fetch fails
+
+                places.append(place_info)
+
+            return json.dumps(places)
+
+        except Exception as e:
+            print(f"Error searching Google Maps: {str(e)}")
+            return str([])
+
+    def get_directions(
+        self,
+        origin: str,
+        destination: str,
+        mode: str = "driving",
+        departure_time: Optional[datetime] = None,
+        avoid: Optional[List[str]] = None,
+    ) -> str:
+        """
+        Get directions between two locations using Google Maps Directions API.
+
+        Args:
+            origin (str): Starting point address or coordinates
+            destination (str): Destination address or coordinates
+            mode (str, optional): Travel mode. Options: "driving", "walking", "bicycling", "transit". Defaults to "driving"
+            departure_time (datetime, optional): Desired departure time for transit directions
+            avoid (List[str], optional): Features to avoid: "tolls", "highways", "ferries"
+
+        Returns:
+            str: Stringified dictionary containing route information including steps, distance, duration, etc.
+        """
+        try:
+            result = self.client.directions(origin, destination, mode=mode, departure_time=departure_time, avoid=avoid)
+            return str(result)
+        except Exception as e:
+            print(f"Error getting directions: {str(e)}")
+            return str([])
+
+    def validate_address(
+        self, address: str, region_code: str = "US", locality: Optional[str] = None, enable_usps_cass: bool = False
+    ) -> str:
+        """
+        Validate an address using Google Maps Address Validation API.
+
+        Args:
+            address (str): The address to validate
+            region_code (str): The region code (e.g., "US" for United States)
+            locality (str, optional): The locality (city) to help with validation
+            enable_usps_cass (bool): Whether to enable USPS CASS validation for US addresses
+
+        Returns:
+            str: Stringified dictionary containing address validation results
+        """
+        try:
+            result = self.client.addressvalidation(
+                [address], regionCode=region_code, locality=locality, enableUspsCass=enable_usps_cass
+            )
+            return str(result)
+        except Exception as e:
+            print(f"Error validating address: {str(e)}")
+            return str({})
+
+    def geocode_address(self, address: str, region: Optional[str] = None) -> str:
+        """
+        Convert an address into geographic coordinates using Google Maps Geocoding API.
+
+        Args:
+            address (str): The address to geocode
+            region (str, optional): The region code to bias results
+
+        Returns:
+            str: Stringified list of dictionaries containing location information
+        """
+        try:
+            result = self.client.geocode(address, region=region)
+            return str(result)
+        except Exception as e:
+            print(f"Error geocoding address: {str(e)}")
+            return str([])
+
+    def reverse_geocode(
+        self, lat: float, lng: float, result_type: Optional[List[str]] = None, location_type: Optional[List[str]] = None
+    ) -> str:
+        """
+        Convert geographic coordinates into an address using Google Maps Reverse Geocoding API.
+
+        Args:
+            lat (float): Latitude
+            lng (float): Longitude
+            result_type (List[str], optional): Array of address types to filter results
+            location_type (List[str], optional): Array of location types to filter results
+
+        Returns:
+            str: Stringified list of dictionaries containing address information
+        """
+        try:
+            result = self.client.reverse_geocode((lat, lng), result_type=result_type, location_type=location_type)
+            return str(result)
+        except Exception as e:
+            print(f"Error reverse geocoding: {str(e)}")
+            return str([])
+
+    def get_distance_matrix(
+        self,
+        origins: List[str],
+        destinations: List[str],
+        mode: str = "driving",
+        departure_time: Optional[datetime] = None,
+        avoid: Optional[List[str]] = None,
+    ) -> str:
+        """
+        Calculate distance and time for a matrix of origins and destinations.
+
+        Args:
+            origins (List[str]): List of addresses or coordinates
+            destinations (List[str]): List of addresses or coordinates
+            mode (str, optional): Travel mode. Options: "driving", "walking", "bicycling", "transit"
+            departure_time (datetime, optional): Desired departure time
+            avoid (List[str], optional): Features to avoid: "tolls", "highways", "ferries"
+
+        Returns:
+            str: Stringified dictionary containing distance and duration information
+        """
+        try:
+            result = self.client.distance_matrix(
+                origins, destinations, mode=mode, departure_time=departure_time, avoid=avoid
+            )
+            return str(result)
+        except Exception as e:
+            print(f"Error getting distance matrix: {str(e)}")
+            return str({})
+
+    def get_elevation(self, lat: float, lng: float) -> str:
+        """
+        Get the elevation for a specific location using Google Maps Elevation API.
+
+        Args:
+            lat (float): Latitude
+            lng (float): Longitude
+
+        Returns:
+            str: Stringified dictionary containing elevation data
+        """
+        try:
+            result = self.client.elevation((lat, lng))
+            return str(result)
+        except Exception as e:
+            print(f"Error getting elevation: {str(e)}")
+            return str([])
+
+    def get_timezone(self, lat: float, lng: float, timestamp: Optional[datetime] = None) -> str:
+        """
+        Get timezone information for a location using Google Maps Time Zone API.
+
+        Args:
+            lat (float): Latitude
+            lng (float): Longitude
+            timestamp (datetime, optional): The timestamp to use for timezone calculation
+
+        Returns:
+            str: Stringified dictionary containing timezone information
+        """
+        try:
+            if timestamp is None:
+                timestamp = datetime.now()
+
+            result = self.client.timezone(location=(lat, lng), timestamp=timestamp)
+            return str(result)
+        except Exception as e:
+            print(f"Error getting timezone: {str(e)}")
+            return str({})
```

### libs/agno/agno/tools/zoom.py

```diff
index fe9f9b5a..bbc17b1f 100644
--- a/libs/agno/agno/tools/zoom.py
+++ b/libs/agno/agno/tools/zoom.py
@@ -1,4 +1,7 @@
 import json
+from base64 import b64encode
+from datetime import datetime, timedelta
+from os import getenv
 from typing import Optional
 
 import requests
@@ -13,25 +16,29 @@ class ZoomTools(Toolkit):
         account_id: Optional[str] = None,
         client_id: Optional[str] = None,
         client_secret: Optional[str] = None,
-        name: str = "zoom_tool",
     ):
         """
         Initialize the ZoomTool.
 
         Args:
-            account_id (str): The Zoom account ID for authentication.
-            client_id (str): The client ID for authentication.
-            client_secret (str): The client secret for authentication.
+            account_id (str): The Zoom account ID for authentication. If not provided, will use ZOOM_ACCOUNT_ID env var.
+            client_id (str): The client ID for authentication. If not provided, will use ZOOM_CLIENT_ID env var.
+            client_secret (str): The client secret for authentication. If not provided, will use ZOOM_CLIENT_SECRET env var.
             name (str): The name of the tool. Defaults to "zoom_tool".
         """
-        super().__init__(name)
-        self.account_id = account_id
-        self.client_id = client_id
-        self.client_secret = client_secret
+        super().__init__("zoom_tool")
+
+        # Get credentials from env vars if not provided
+        self.account_id = account_id or getenv("ZOOM_ACCOUNT_ID")
+        self.client_id = client_id or getenv("ZOOM_CLIENT_ID")
+        self.client_secret = client_secret or getenv("ZOOM_CLIENT_SECRET")
         self.__access_token = None  # Made private
+        self.__token_expiry = None  # Track token expiration
 
         if not self.account_id or not self.client_id or not self.client_secret:
-            logger.error("ZOOM_ACCOUNT_ID, ZOOM_CLIENT_ID, and ZOOM_CLIENT_SECRET must be set.")
+            logger.error(
+                "ZOOM_ACCOUNT_ID, ZOOM_CLIENT_ID, and ZOOM_CLIENT_SECRET must be set either through parameters or environment variables."
+            )
 
         # Register functions
         self.register(self.schedule_meeting)
@@ -42,8 +49,47 @@ class ZoomTools(Toolkit):
         self.register(self.get_meeting)
 
     def get_access_token(self) -> str:
-        """Get the current access token"""
-        return str(self.__access_token) if self.__access_token else ""
+        """
+        Get a valid access token, refreshing if necessary using Zoom's Server-to-Server OAuth.
+
+        Returns:
+            str: The current access token or empty string if token generation fails.
+        """
+        # Check if we have a valid token
+        if self.__access_token and self.__token_expiry and datetime.now() < self.__token_expiry:
+            return self.__access_token
+
+        # Generate new token
+        try:
+            headers = {
+                "Content-Type": "application/x-www-form-urlencoded",
+            }
+
+            # Create base64 encoded auth string
+            auth_string = b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode()
+            headers["Authorization"] = f"Basic {auth_string}"
+
+            data = {
+                "grant_type": "account_credentials",
+                "account_id": self.account_id,
+            }
+
+            response = requests.post("https://zoom.us/oauth/token", headers=headers, data=data)
+            response.raise_for_status()
+
+            token_data = response.json()
+            self.__access_token = token_data["access_token"]
+            # Set expiry time slightly before actual expiry to ensure token validity
+            self.__token_expiry = datetime.now() + timedelta(seconds=token_data["expires_in"] - 60)  # type: ignore
+
+            logger.debug("Successfully generated new Zoom access token")
+            return self.__access_token  # type: ignore
+
+        except requests.RequestException as e:
+            logger.error(f"Failed to generate Zoom access token: {e}")
+            self.__access_token = None
+            self.__token_expiry = None
+            return ""
 
     def schedule_meeting(self, topic: str, start_time: str, duration: int, timezone: str = "UTC") -> str:
         """
@@ -223,7 +269,7 @@ class ZoomTools(Toolkit):
 
             result = {
                 "message": "Meeting recordings retrieved successfully",
-                "meeting_id": recordings.get("id", ""),
+                "meeting_id": str(recordings.get("id", "")),
                 "uuid": recordings.get("uuid", ""),
                 "host_id": recordings.get("host_id", ""),
                 "topic": recordings.get("topic", ""),
@@ -306,7 +352,7 @@ class ZoomTools(Toolkit):
 
             result = {
                 "message": "Meeting details retrieved successfully",
-                "meeting_id": meeting_info.get("id", ""),
+                "meeting_id": str(meeting_info.get("id", "")),
                 "topic": meeting_info.get("topic", ""),
                 "type": meeting_info.get("type", ""),
                 "start_time": meeting_info.get("start_time", ""),
```

### libs/agno/pyproject.toml

```diff
index 0c836093..d306214a 100644
--- a/libs/agno/pyproject.toml
+++ b/libs/agno/pyproject.toml
@@ -1,6 +1,6 @@
 [project]
 name = "agno"
-version = "1.0.5"
+version = "1.0.6"
 description = "Agno: a lightweight framework for building multi-modal Agents"
 requires-python = ">=3.7,<4"
 readme = "README.md"
@@ -202,6 +202,7 @@ module = [
   "firecrawl.*",
   "github.*",
   "google.*",
+  "googlemaps.*",
   "google_auth_oauthlib.*",
   "googleapiclient.*",
   "googlesearch.*",
```

### libs/agno/tests/unit/tools/test_github.py

```diff
new file mode 100644
index 00000000..aa6d7d38
--- /dev/null
+++ b/libs/agno/tests/unit/tools/test_github.py
@@ -0,0 +1,389 @@
+"""Unit tests for GitHub tools."""
+
+import json
+from datetime import datetime
+from unittest.mock import MagicMock, patch
+
+import pytest
+from github import Github
+from github.GithubException import GithubException
+from github.Issue import Issue
+from github.PullRequest import PullRequest
+from github.Repository import Repository
+
+from agno.tools.github import GithubTools
+
+
+@pytest.fixture
+def mock_github():
+    """Create a mock GitHub client."""
+    with patch("agno.tools.github.Github") as mock_github, patch.dict(
+        "os.environ", {"GITHUB_ACCESS_TOKEN": "dummy_token"}
+    ):
+        mock_client = MagicMock(spec=Github)
+        mock_github.return_value = mock_client
+        mock_repo = MagicMock(spec=Repository)
+        mock_repo.full_name = "test-org/test-repo"
+        mock_client.get_repo.return_value = mock_repo
+
+        yield mock_client, mock_repo
+
+
+@pytest.fixture
+def mock_search_repos():
+    """Create mock repositories for search tests."""
+    mock_repo1 = MagicMock(spec=Repository)
+    mock_repo1.full_name = "test-org/awesome-project"
+    mock_repo1.description = "An awesome project"
+    mock_repo1.html_url = "https://github.com/test-org/awesome-project"
+    mock_repo1.stargazers_count = 1000
+    mock_repo1.forks_count = 100
+    mock_repo1.language = "Python"
+
+    mock_repo2 = MagicMock(spec=Repository)
+    mock_repo2.full_name = "test-org/another-project"
+    mock_repo2.description = "Another cool project"
+    mock_repo2.html_url = "https://github.com/test-org/another-project"
+    mock_repo2.stargazers_count = 500
+    mock_repo2.forks_count = 50
+    mock_repo2.language = "JavaScript"
+
+    return [mock_repo1, mock_repo2]
+
+
+@pytest.fixture
+def mock_paginated_list(mock_search_repos):
+    """Create a mock paginated list for search results."""
+    mock_list = MagicMock()
+    mock_list.totalCount = len(mock_search_repos)
+    mock_list.__iter__.return_value = mock_search_repos
+    mock_list.get_page.return_value = mock_search_repos
+    return mock_list
+
+
+def test_list_pull_requests(mock_github):
+    """Test listing pull requests."""
+    mock_client, mock_repo = mock_github
+    github_tools = GithubTools()
+
+    # Mock PR data
+    mock_pr1 = MagicMock(spec=PullRequest)
+    mock_pr1.number = 1
+    mock_pr1.title = "Feature: Add new functionality"
+    mock_pr1.html_url = "https://github.com/test-org/test-repo/pull/1"
+    mock_pr1.state = "open"
+    mock_pr1.user.login = "test-user"
+    mock_pr1.created_at = datetime(2024, 2, 4, 12, 0, 0)
+
+    mock_pr2 = MagicMock(spec=PullRequest)
+    mock_pr2.number = 2
+    mock_pr2.title = "Fix: Bug fix"
+    mock_pr2.html_url = "https://github.com/test-org/test-repo/pull/2"
+    mock_pr2.state = "closed"
+    mock_pr2.user.login = "another-user"
+    mock_pr2.created_at = datetime(2024, 2, 3, 12, 0, 0)
+
+    mock_repo.get_pulls.return_value = [mock_pr1, mock_pr2]
+
+    # Test listing all PRs
+    result = github_tools.list_pull_requests("test-org/test-repo")
+    result_data = json.loads(result)
+
+    assert len(result_data) == 2
+    assert result_data[0]["number"] == 1
+    assert result_data[0]["state"] == "open"
+    assert result_data[1]["number"] == 2
+    assert result_data[1]["state"] == "closed"
+
+    # Test listing only open PRs
+    mock_repo.get_pulls.return_value = [mock_pr1]
+    result = github_tools.list_pull_requests("test-org/test-repo", state="open")
+    result_data = json.loads(result)
+
+    assert len(result_data) == 1
+    assert result_data[0]["state"] == "open"
+
+
+def test_list_issues(mock_github):
+    """Test listing issues."""
+    mock_client, mock_repo = mock_github
+    github_tools = GithubTools()
+
+    # Mock issue data
+    mock_issue1 = MagicMock(spec=Issue)
+    mock_issue1.number = 1
+    mock_issue1.title = "Bug: Something is broken"
+    mock_issue1.html_url = "https://github.com/test-org/test-repo/issues/1"
+    mock_issue1.state = "open"
+    mock_issue1.user.login = "test-user"
+    mock_issue1.pull_request = None
+    mock_issue1.created_at = datetime(2024, 2, 4, 12, 0, 0)
+
+    mock_issue2 = MagicMock(spec=Issue)
+    mock_issue2.number = 2
+    mock_issue2.title = "Enhancement: New feature request"
+    mock_issue2.html_url = "https://github.com/test-org/test-repo/issues/2"
+    mock_issue2.state = "closed"
+    mock_issue2.user.login = "another-user"
+    mock_issue2.pull_request = None
+    mock_issue2.created_at = datetime(2024, 2, 3, 12, 0, 0)
+
+    mock_repo.get_issues.return_value = [mock_issue1, mock_issue2]
+
+    # Test listing all issues
+    result = github_tools.list_issues("test-org/test-repo")
+    result_data = json.loads(result)
+
+    assert len(result_data) == 2
+    assert result_data[0]["number"] == 1
+    assert result_data[0]["state"] == "open"
+    assert result_data[1]["number"] == 2
+    assert result_data[1]["state"] == "closed"
+
+    # Test listing only open issues
+    mock_repo.get_issues.return_value = [mock_issue1]
+    result = github_tools.list_issues("test-org/test-repo", state="open")
+    result_data = json.loads(result)
+
+    assert len(result_data) == 1
+    assert result_data[0]["state"] == "open"
+
+
+def test_create_issue(mock_github):
+    """Test creating an issue."""
+    mock_client, mock_repo = mock_github
+    github_tools = GithubTools()
+
+    mock_issue = MagicMock(spec=Issue)
+    mock_issue.id = 123
+    mock_issue.number = 1
+    mock_issue.title = "New Issue"
+    mock_issue.html_url = "https://github.com/test-org/test-repo/issues/1"
+    mock_issue.state = "open"
+    mock_issue.user.login = "test-user"
+    mock_issue.body = "Issue description"
+    mock_issue.created_at = datetime(2024, 2, 4, 12, 0, 0)
+
+    mock_repo.create_issue.return_value = mock_issue
+
+    result = github_tools.create_issue("test-org/test-repo", title="New Issue", body="Issue description")
+    result_data = json.loads(result)
+
+    mock_repo.create_issue.assert_called_once_with(title="New Issue", body="Issue description")
+    assert result_data["id"] == 123
+    assert result_data["number"] == 1
+    assert result_data["title"] == "New Issue"
+    assert result_data["state"] == "open"
+
+
+def test_get_repository(mock_github):
+    """Test getting repository information."""
+    mock_client, mock_repo = mock_github
+    github_tools = GithubTools()
+
+    # Mock repository data
+    mock_repo.full_name = "test-org/test-repo"
+    mock_repo.description = "Test repository"
+    mock_repo.html_url = "https://github.com/test-org/test-repo"
+    mock_repo.stargazers_count = 100
+    mock_repo.forks_count = 50
+    mock_repo.open_issues_count = 10
+    mock_repo.default_branch = "main"
+    mock_repo.private = False
+    mock_repo.language = "Python"
+    mock_repo.license = MagicMock()
+    mock_repo.license.name = "MIT"
+
+    result = github_tools.get_repository("test-org/test-repo")
+    result_data = json.loads(result)
+
+    assert result_data["name"] == "test-org/test-repo"
+    assert result_data["description"] == "Test repository"
+    assert result_data["stars"] == 100
+    assert result_data["forks"] == 50
+    assert result_data["open_issues"] == 10
+    assert result_data["language"] == "Python"
+    assert result_data["license"] == "MIT"
+
+
+def test_error_handling(mock_github):
+    """Test error handling for various scenarios."""
+    mock_client, mock_repo = mock_github
+    github_tools = GithubTools()
+
+    # Test repository not found
+    mock_client.get_repo.side_effect = GithubException(status=404, data={"message": "Repository not found"})
+    result = github_tools.get_repository("invalid/repo")
+    result_data = json.loads(result)
+    assert "error" in result_data
+    assert "Repository not found" in result_data["error"]
+
+    # Reset side effect
+    mock_client.get_repo.side_effect = None
+
+    # Test permission error for creating issues
+    mock_repo.create_issue.side_effect = GithubException(status=403, data={"message": "Permission denied"})
+    result = github_tools.create_issue("test-org/test-repo", title="Test")
+    result_data = json.loads(result)
+    assert "error" in result_data
+    assert "Permission denied" in result_data["error"]
+
+
+def test_search_repositories_basic(mock_github, mock_paginated_list):
+    """Test basic repository search functionality."""
+    mock_client, _ = mock_github
+    github_tools = GithubTools()
+
+    mock_client.search_repositories.return_value = mock_paginated_list
+
+    result = github_tools.search_repositories("awesome python")
+    result_data = json.loads(result)
+
+    mock_client.search_repositories.assert_called_once_with(query="awesome python", sort="stars", order="desc")
+    assert len(result_data) == 2
+    assert "full_name" in result_data[0]
+    assert "description" in result_data[0]
+    assert "url" in result_data[0]
+    assert "stars" in result_data[0]
+    assert "forks" in result_data[0]
+    assert "language" in result_data[0]
+
+
+def test_search_repositories_empty_results(mock_github):
+    """Test repository search with no results."""
+    mock_client, _ = mock_github
+    github_tools = GithubTools()
+
+    mock_empty_list = MagicMock()
+    mock_empty_list.totalCount = 0
+    mock_empty_list.__iter__.return_value = []
+    mock_empty_list.get_page.return_value = []
+    mock_client.search_repositories.return_value = mock_empty_list
+
+    result = github_tools.search_repositories("nonexistent-repo-name")
+    result_data = json.loads(result)
+    assert len(result_data) == 0
+
+
+def test_search_repositories_with_sorting(mock_github, mock_paginated_list):
+    """Test repository search with sorting parameters."""
+    mock_client, _ = mock_github
+    github_tools = GithubTools()
+
+    mock_client.search_repositories.return_value = mock_paginated_list
+
+    result = github_tools.search_repositories("python", sort="stars", order="desc")
+    result_data = json.loads(result)
+
+    mock_client.search_repositories.assert_called_with(query="python", sort="stars", order="desc")
+    assert len(result_data) == 2
+    assert result_data[0]["stars"] == 1000
+    assert result_data[1]["stars"] == 500
+
+
+def test_search_repositories_with_language_filter(mock_github, mock_paginated_list):
+    """Test repository search with language filter."""
+    mock_client, _ = mock_github
+    github_tools = GithubTools()
+
+    mock_client.search_repositories.return_value = mock_paginated_list
+
+    result = github_tools.search_repositories("project language:python")
+    result_data = json.loads(result)
+
+    mock_client.search_repositories.assert_called_with(query="project language:python", sort="stars", order="desc")
+    assert len(result_data) == 2
+
+
+def test_search_repositories_rate_limit_error(mock_github):
+    """Test repository search with rate limit error."""
+    mock_client, _ = mock_github
+    github_tools = GithubTools()
+
+    mock_client.search_repositories.side_effect = GithubException(
+        status=403, data={"message": "API rate limit exceeded"}
+    )
+
+    result = github_tools.search_repositories("python")
+    result_data = json.loads(result)
+    assert "error" in result_data
+    assert "API rate limit exceeded" in result_data["error"]
+
+
+def test_search_repositories_pagination(mock_github):
+    """Test repository search with pagination."""
+    mock_client, _ = mock_github
+    github_tools = GithubTools()
+
+    # Create mock repos for different pages
+    mock_repos_page1 = [
+        MagicMock(
+            full_name="test-org/repo1",
+            description="First repo",
+            html_url="https://github.com/test-org/repo1",
+            stargazers_count=1000,
+            forks_count=100,
+            language="Python",
+        ),
+        MagicMock(
+            full_name="test-org/repo2",
+            description="Second repo",
+            html_url="https://github.com/test-org/repo2",
+            stargazers_count=900,
+            forks_count=90,
+            language="Python",
+        ),
+    ]
+
+    mock_repos_page2 = [
+        MagicMock(
+            full_name="test-org/repo3",
+            description="Third repo",
+            html_url="https://github.com/test-org/repo3",
+            stargazers_count=800,
+            forks_count=80,
+            language="Python",
+        )
+    ]
+
+    # Mock paginated list
+    mock_paginated = MagicMock()
+    mock_paginated.totalCount = 3
+
+    # Test first page
+    mock_paginated.get_page.return_value = mock_repos_page1
+    mock_client.search_repositories.return_value = mock_paginated
+
+    result = github_tools.search_repositories("python", page=1, per_page=2)
+    result_data = json.loads(result)
+
+    mock_paginated.get_page.assert_called_with(0)  # GitHub API uses 0-based indexing
+    assert len(result_data) == 2
+    assert result_data[0]["full_name"] == "test-org/repo1"
+    assert result_data[1]["full_name"] == "test-org/repo2"
+
+    # Test second page
+    mock_paginated.get_page.return_value = mock_repos_page2
+    mock_client.search_repositories.return_value = mock_paginated
+
+    result = github_tools.search_repositories("python", page=2, per_page=2)
+    result_data = json.loads(result)
+
+    mock_paginated.get_page.assert_called_with(1)  # GitHub API uses 0-based indexing
+    assert len(result_data) == 1
+    assert result_data[0]["full_name"] == "test-org/repo3"
+
+    # Test with custom per_page
+    mock_paginated.get_page.return_value = mock_repos_page1[:1]
+    result = github_tools.search_repositories("python", page=1, per_page=1)
+    result_data = json.loads(result)
+
+    assert len(result_data) == 1
+    assert result_data[0]["full_name"] == "test-org/repo1"
+
+    # Test with per_page exceeding GitHub's max (100)
+    result = github_tools.search_repositories("python", per_page=150)
+    result_data = json.loads(result)
+
+    # Should be limited to 100
+    mock_client.search_repositories.assert_called_with(query="python", sort="stars", order="desc")
```

### libs/agno/tests/unit/tools/test_google_maps.py

```diff
new file mode 100644
index 00000000..7e4633b0
--- /dev/null
+++ b/libs/agno/tests/unit/tools/test_google_maps.py
@@ -0,0 +1,317 @@
+"""Unit tests for Google Maps tools."""
+
+import json
+from datetime import datetime
+from unittest.mock import patch
+
+import pytest
+
+from agno.tools.google_maps import GoogleMapTools
+
+# Mock responses
+MOCK_PLACES_RESPONSE = {
+    "results": [
+        {
+            "name": "Test Business",
+            "formatted_address": "123 Test St, Test City",
+            "rating": 4.5,
+            "user_ratings_total": 100,
+            "place_id": "test_place_id",
+        }
+    ]
+}
+
+MOCK_PLACE_DETAILS = {
+    "result": {
+        "formatted_phone_number": "123-456-7890",
+        "website": "https://test.com",
+        "opening_hours": {"weekday_text": ["Monday: 9:00 AM – 5:00 PM"]},
+    }
+}
+
+MOCK_DIRECTIONS_RESPONSE = [
+    {
+        "legs": [
+            {
+                "distance": {"text": "5 km", "value": 5000},
+                "duration": {"text": "10 mins", "value": 600},
+                "steps": [],
+            }
+        ]
+    }
+]
+
+MOCK_ADDRESS_VALIDATION_RESPONSE = {
+    "result": {
+        "verdict": {"validationGranularity": "PREMISE", "hasInferredComponents": False},
+        "address": {"formattedAddress": "123 Test St, Test City, ST 12345"},
+    }
+}
+
+MOCK_GEOCODE_RESPONSE = [
+    {
+        "formatted_address": "123 Test St, Test City, ST 12345",
+        "geometry": {"location": {"lat": 40.7128, "lng": -74.0060}},
+    }
+]
+
+MOCK_DISTANCE_MATRIX_RESPONSE = {
+    "rows": [
+        {
+            "elements": [
+                {
+                    "distance": {"text": "5 km", "value": 5000},
+                    "duration": {"text": "10 mins", "value": 600},
+                }
+            ]
+        }
+    ]
+}
+
+MOCK_ELEVATION_RESPONSE = [{"elevation": 100.0}]
+
+MOCK_TIMEZONE_RESPONSE = {
+    "timeZoneId": "America/New_York",
+    "timeZoneName": "Eastern Daylight Time",
+}
+
+
+@pytest.fixture
+def google_maps_tools():
+    """Create a GoogleMapTools instance with a mock API key."""
+    with patch.dict("os.environ", {"GOOGLE_MAPS_API_KEY": "AIzaTest"}):
+        return GoogleMapTools()
+
+
+@pytest.fixture
+def mock_client():
+    """Create a mock Google Maps client."""
+    with patch("googlemaps.Client") as mock:
+        yield mock
+
+
+def test_search_places(google_maps_tools):
+    """Test the search_places method."""
+    with patch.object(google_maps_tools.client, "places") as mock_places:
+        with patch.object(google_maps_tools.client, "place") as mock_place:
+            mock_places.return_value = MOCK_PLACES_RESPONSE
+            mock_place.return_value = MOCK_PLACE_DETAILS
+
+            result = json.loads(google_maps_tools.search_places("test query"))
+
+            assert len(result) == 1
+            assert result[0]["name"] == "Test Business"
+            assert result[0]["phone"] == "123-456-7890"
+            assert result[0]["website"] == "https://test.com"
+
+
+def test_get_directions(google_maps_tools):
+    """Test the get_directions method."""
+    with patch.object(google_maps_tools.client, "directions") as mock_directions:
+        mock_directions.return_value = MOCK_DIRECTIONS_RESPONSE
+
+        result = eval(google_maps_tools.get_directions(origin="Test Origin", destination="Test Destination"))
+
+        assert isinstance(result, list)
+        assert "legs" in result[0]
+        assert result[0]["legs"][0]["distance"]["value"] == 5000
+
+
+def test_validate_address(google_maps_tools):
+    """Test the validate_address method."""
+    with patch.object(google_maps_tools.client, "addressvalidation") as mock_validate:
+        mock_validate.return_value = MOCK_ADDRESS_VALIDATION_RESPONSE
+
+        result = eval(google_maps_tools.validate_address("123 Test St"))
+
+        assert isinstance(result, dict)
+        assert "result" in result
+        assert "verdict" in result["result"]
+
+
+def test_geocode_address(google_maps_tools):
+    """Test the geocode_address method."""
+    with patch.object(google_maps_tools.client, "geocode") as mock_geocode:
+        mock_geocode.return_value = MOCK_GEOCODE_RESPONSE
+
+        result = eval(google_maps_tools.geocode_address("123 Test St"))
+
+        assert isinstance(result, list)
+        assert result[0]["formatted_address"] == "123 Test St, Test City, ST 12345"
+
+
+def test_reverse_geocode(google_maps_tools):
+    """Test the reverse_geocode method."""
+    with patch.object(google_maps_tools.client, "reverse_geocode") as mock_reverse:
+        mock_reverse.return_value = MOCK_GEOCODE_RESPONSE
+
+        result = eval(google_maps_tools.reverse_geocode(40.7128, -74.0060))
+
+        assert isinstance(result, list)
+        assert result[0]["formatted_address"] == "123 Test St, Test City, ST 12345"
+
+
+def test_get_distance_matrix(google_maps_tools):
+    """Test the get_distance_matrix method."""
+    with patch.object(google_maps_tools.client, "distance_matrix") as mock_matrix:
+        mock_matrix.return_value = MOCK_DISTANCE_MATRIX_RESPONSE
+
+        result = eval(google_maps_tools.get_distance_matrix(origins=["Origin"], destinations=["Destination"]))
+
+        assert isinstance(result, dict)
+        assert "rows" in result
+        assert result["rows"][0]["elements"][0]["distance"]["value"] == 5000
+
+
+def test_get_elevation(google_maps_tools):
+    """Test the get_elevation method."""
+    with patch.object(google_maps_tools.client, "elevation") as mock_elevation:
+        mock_elevation.return_value = MOCK_ELEVATION_RESPONSE
+
+        result = eval(google_maps_tools.get_elevation(40.7128, -74.0060))
+
+        assert isinstance(result, list)
+        assert result[0]["elevation"] == 100.0
+
+
+def test_get_timezone(google_maps_tools):
+    """Test the get_timezone method."""
+    with patch.object(google_maps_tools.client, "timezone") as mock_timezone:
+        mock_timezone.return_value = MOCK_TIMEZONE_RESPONSE
+        test_time = datetime(2024, 1, 1, 12, 0)
+
+        result = eval(google_maps_tools.get_timezone(40.7128, -74.0060, test_time))
+
+        assert isinstance(result, dict)
+        assert result["timeZoneId"] == "America/New_York"
+
+
+def test_error_handling(google_maps_tools):
+    """Test error handling in various methods."""
+    with patch.object(google_maps_tools.client, "places") as mock_places:
+        mock_places.side_effect = Exception("API Error")
+
+        result = google_maps_tools.search_places("test query")
+        assert result == "[]"
+
+    with patch.object(google_maps_tools.client, "directions") as mock_directions:
+        mock_directions.side_effect = Exception("API Error")
+
+        result = google_maps_tools.get_directions("origin", "destination")
+        assert result == "[]"
+
+
+def test_initialization_without_api_key():
+    """Test initialization without API key."""
+    with patch.dict("os.environ", clear=True):
+        with pytest.raises(ValueError, match="GOOGLE_MAPS_API_KEY is not set"):
+            GoogleMapTools()
+
+
+def test_initialization_with_selective_tools():
+    """Test initialization with only selected tools."""
+    with patch.dict("os.environ", {"GOOGLE_MAPS_API_KEY": "AIzaTest"}):
+        tools = GoogleMapTools(
+            search_places=True,
+            get_directions=False,
+            validate_address=False,
+            geocode_address=True,
+            reverse_geocode=False,
+            get_distance_matrix=False,
+            get_elevation=False,
+            get_timezone=False,
+        )
+
+        assert "search_places" in [func.name for func in tools.functions.values()]
+        assert "get_directions" not in [func.name for func in tools.functions.values()]
+        assert "geocode_address" in [func.name for func in tools.functions.values()]
+
+
+def test_search_places_success(google_maps_tools):
+    """Test the search_places method with successful response."""
+    with patch.object(google_maps_tools.client, "places") as mock_places:
+        with patch.object(google_maps_tools.client, "place") as mock_place:
+            mock_places.return_value = MOCK_PLACES_RESPONSE
+            mock_place.return_value = MOCK_PLACE_DETAILS
+
+            result = json.loads(google_maps_tools.search_places("test query"))
+
+            assert len(result) == 1
+            assert result[0]["name"] == "Test Business"
+            assert result[0]["phone"] == "123-456-7890"
+            assert result[0]["website"] == "https://test.com"
+            mock_places.assert_called_once_with("test query")
+            mock_place.assert_called_once_with("test_place_id")
+
+
+def test_search_places_no_results(google_maps_tools):
+    """Test search_places when no results are returned."""
+    with patch.object(google_maps_tools.client, "places") as mock_places:
+        mock_places.return_value = {"results": []}
+        result = json.loads(google_maps_tools.search_places("test query"))
+        assert result == []
+
+
+def test_search_places_none_response(google_maps_tools):
+    """Test search_places when None is returned."""
+    with patch.object(google_maps_tools.client, "places") as mock_places:
+        mock_places.return_value = None
+        result = json.loads(google_maps_tools.search_places("test query"))
+        assert result == []
+
+
+def test_search_places_missing_results_key(google_maps_tools):
+    """Test search_places when response is missing results key."""
+    with patch.object(google_maps_tools.client, "places") as mock_places:
+        mock_places.return_value = {"status": "OK"}
+        result = json.loads(google_maps_tools.search_places("test query"))
+        assert result == []
+
+
+def test_search_places_missing_place_id(google_maps_tools):
+    """Test search_places when place_id is missing."""
+    with patch.object(google_maps_tools.client, "places") as mock_places:
+        mock_places.return_value = {
+            "results": [
+                {
+                    "name": "Test Business",
+                    "formatted_address": "123 Test St",
+                    "rating": 4.5,
+                }
+            ]
+        }
+        result = json.loads(google_maps_tools.search_places("test query"))
+        assert len(result) == 1
+        assert result[0]["name"] == "Test Business"
+        assert "phone" not in result[0]
+        assert "website" not in result[0]
+
+
+def test_search_places_invalid_details(google_maps_tools):
+    """Test search_places when place details are invalid."""
+    with patch.object(google_maps_tools.client, "places") as mock_places:
+        with patch.object(google_maps_tools.client, "place") as mock_place:
+            mock_places.return_value = MOCK_PLACES_RESPONSE
+            mock_place.return_value = {"status": "NOT_FOUND"}  # Missing 'result' key
+
+            result = json.loads(google_maps_tools.search_places("test query"))
+
+            assert len(result) == 1
+            assert result[0]["name"] == "Test Business"
+            assert "phone" not in result[0]
+            assert "website" not in result[0]
+
+
+def test_search_places_details_error(google_maps_tools):
+    """Test search_places when place details call raises an error."""
+    with patch.object(google_maps_tools.client, "places") as mock_places:
+        with patch.object(google_maps_tools.client, "place") as mock_place:
+            mock_places.return_value = MOCK_PLACES_RESPONSE
+            mock_place.side_effect = Exception("API Error")
+
+            result = json.loads(google_maps_tools.search_places("test query"))
+
+            assert len(result) == 1
+            assert result[0]["name"] == "Test Business"
+            assert "phone" not in result[0]
+            assert "website" not in result[0]
```

### libs/agno/tests/unit/tools/test_zoom_tools.py

```diff
new file mode 100644
index 00000000..017d2590
--- /dev/null
+++ b/libs/agno/tests/unit/tools/test_zoom_tools.py
@@ -0,0 +1,356 @@
+import json
+from datetime import datetime, timedelta
+from unittest.mock import MagicMock, patch
+
+import pytest
+import requests
+
+from agno.tools.zoom import ZoomTools
+
+
+@pytest.fixture
+def zoom_tools():
+    """Create a ZoomTools instance with mock credentials"""
+    return ZoomTools(
+        account_id="test_account_id",
+        client_id="test_client_id",
+        client_secret="test_client_secret",
+    )
+
+
+@pytest.fixture
+def mock_token_response():
+    """Mock successful token response"""
+    return {
+        "access_token": "test_access_token",
+        "token_type": "bearer",
+        "expires_in": 3600,
+    }
+
+
+def test_init_with_credentials():
+    """Test initialization with provided credentials"""
+    tool = ZoomTools(
+        account_id="test_account_id",
+        client_id="test_client_id",
+        client_secret="test_client_secret",
+    )
+    assert tool.account_id == "test_account_id"
+    assert tool.client_id == "test_client_id"
+    assert tool.client_secret == "test_client_secret"
+
+
+@patch.dict(
+    "os.environ",
+    {
+        "ZOOM_ACCOUNT_ID": "env_account_id",
+        "ZOOM_CLIENT_ID": "env_client_id",
+        "ZOOM_CLIENT_SECRET": "env_client_secret",
+    },
+)
+def test_init_with_env_vars():
+    """Test initialization with environment variables"""
+    tool = ZoomTools()
+    assert tool.account_id == "env_account_id"
+    assert tool.client_id == "env_client_id"
+    assert tool.client_secret == "env_client_secret"
+
+
+def test_get_access_token_success(zoom_tools, mock_token_response):
+    """Test successful access token generation"""
+    with patch("requests.post") as mock_post:
+        mock_post.return_value.json.return_value = mock_token_response
+        mock_post.return_value.raise_for_status = MagicMock()
+
+        token = zoom_tools.get_access_token()
+
+        assert token == "test_access_token"
+        mock_post.assert_called_once()
+
+        # Verify request format
+        args, kwargs = mock_post.call_args
+        assert args[0] == "https://zoom.us/oauth/token"
+        assert kwargs["headers"]["Content-Type"] == "application/x-www-form-urlencoded"
+        assert kwargs["data"]["grant_type"] == "account_credentials"
+        assert kwargs["data"]["account_id"] == "test_account_id"
+
+
+def test_get_access_token_reuse(zoom_tools, mock_token_response):
+    """Test token reuse when not expired"""
+    with patch("requests.post") as mock_post:
+        mock_post.return_value.json.return_value = mock_token_response
+        mock_post.return_value.raise_for_status = MagicMock()
+
+        # First call should make the request
+        token1 = zoom_tools.get_access_token()
+        assert token1 == "test_access_token"
+        assert mock_post.call_count == 1
+
+        # Second call should reuse the token
+        token2 = zoom_tools.get_access_token()
+        assert token2 == "test_access_token"
+        assert mock_post.call_count == 1  # No additional calls
+
+
+def test_get_access_token_refresh_on_expiry(zoom_tools, mock_token_response):
+    """Test token refresh when expired"""
+    with patch("requests.post") as mock_post:
+        mock_post.return_value.json.return_value = mock_token_response
+        mock_post.return_value.raise_for_status = MagicMock()
+
+        # Get initial token
+        token1 = zoom_tools.get_access_token()
+        assert token1 == "test_access_token"
+
+        # Manually expire the token
+        zoom_tools._ZoomTools__token_expiry = datetime.now() - timedelta(seconds=1)
+
+        # Should get new token
+        token2 = zoom_tools.get_access_token()
+        assert token2 == "test_access_token"
+        assert mock_post.call_count == 2
+
+
+def test_get_access_token_failure(zoom_tools):
+    """Test handling of token generation failure"""
+    with patch("requests.post") as mock_post:
+        mock_post.side_effect = requests.RequestException("API Error")
+
+        token = zoom_tools.get_access_token()
+        assert token == ""
+        assert zoom_tools._ZoomTools__access_token is None
+        assert zoom_tools._ZoomTools__token_expiry is None
+
+
+@pytest.mark.parametrize(
+    "method_name,expected_args",
+    [
+        (
+            "schedule_meeting",
+            {"topic": "Test Meeting", "start_time": "2024-02-01T10:00:00Z", "duration": 60, "timezone": "UTC"},
+        ),
+        ("get_upcoming_meetings", {"user_id": "me"}),
+        ("list_meetings", {"user_id": "me", "type": "scheduled"}),
+        ("get_meeting_recordings", {"meeting_id": "123456789"}),
+        ("delete_meeting", {"meeting_id": "123456789"}),
+        ("get_meeting", {"meeting_id": "123456789"}),
+    ],
+)
+def test_api_methods_auth_failure(zoom_tools, method_name, expected_args):
+    """Test API methods handle authentication failure gracefully"""
+    with patch.object(ZoomTools, "get_access_token", return_value=""):
+        method = getattr(zoom_tools, method_name)
+        result = method(**expected_args)
+        error_response = json.loads(result)
+        assert "error" in error_response
+        assert error_response["error"] == "Failed to obtain access token"
+
+
+def test_schedule_meeting_success(zoom_tools):
+    """Test successful meeting scheduling"""
+    mock_response = {
+        "id": 123456789,
+        "topic": "Test Meeting",
+        "start_time": "2024-02-01T10:00:00Z",
+        "duration": 60,
+        "join_url": "https://zoom.us/j/123456789",
+    }
+
+    with patch.object(ZoomTools, "get_access_token", return_value="test_token"), patch("requests.post") as mock_post:
+        mock_post.return_value.json.return_value = mock_response
+        mock_post.return_value.raise_for_status = MagicMock()
+
+        result = zoom_tools.schedule_meeting(topic="Test Meeting", start_time="2024-02-01T10:00:00Z", duration=60)
+
+        result_data = json.loads(result)
+        assert result_data["meeting_id"] == 123456789
+        assert result_data["topic"] == "Test Meeting"
+        assert result_data["join_url"] == "https://zoom.us/j/123456789"
+
+
+def test_get_meeting_success(zoom_tools):
+    """Test successful meeting retrieval"""
+    mock_response = {
+        "id": 123456789,
+        "topic": "Test Meeting",
+        "type": 2,
+        "start_time": "2024-02-01T10:00:00Z",
+        "duration": 60,
+        "timezone": "UTC",
+        "created_at": "2024-01-31T10:00:00Z",
+        "join_url": "https://zoom.us/j/123456789",
+        "settings": {"host_video": True},
+    }
+
+    with patch.object(ZoomTools, "get_access_token", return_value="test_token"), patch("requests.get") as mock_get:
+        mock_get.return_value.json.return_value = mock_response
+        mock_get.return_value.raise_for_status = MagicMock()
+
+        result = zoom_tools.get_meeting("123456789")
+
+        result_data = json.loads(result)
+        assert result_data["meeting_id"] == "123456789"
+        assert result_data["topic"] == "Test Meeting"
+        assert result_data["join_url"] == "https://zoom.us/j/123456789"
+
+
+def test_get_upcoming_meetings_success(zoom_tools):
+    """Test successful retrieval of upcoming meetings"""
+    mock_response = {
+        "page_count": 1,
+        "page_number": 1,
+        "page_size": 30,
+        "total_records": 2,
+        "meetings": [
+            {
+                "id": 123456789,
+                "topic": "Meeting 1",
+                "start_time": "2024-02-01T10:00:00Z",
+            },
+            {
+                "id": 987654321,
+                "topic": "Meeting 2",
+                "start_time": "2024-02-02T15:00:00Z",
+            },
+        ],
+    }
+
+    with patch.object(ZoomTools, "get_access_token", return_value="test_token"), patch("requests.get") as mock_get:
+        mock_get.return_value.json.return_value = mock_response
+        mock_get.return_value.raise_for_status = MagicMock()
+
+        result = zoom_tools.get_upcoming_meetings()
+        result_data = json.loads(result)
+
+        assert result_data["message"] == "Upcoming meetings retrieved successfully"
+        assert len(result_data["meetings"]) == 2
+        assert result_data["meetings"][0]["id"] == 123456789
+        assert result_data["meetings"][1]["id"] == 987654321
+
+
+def test_list_meetings_success(zoom_tools):
+    """Test successful listing of meetings"""
+    mock_response = {
+        "page_count": 1,
+        "page_number": 1,
+        "page_size": 30,
+        "total_records": 2,
+        "meetings": [
+            {
+                "id": 123456789,
+                "topic": "Scheduled Meeting 1",
+                "type": 2,
+                "start_time": "2024-02-01T10:00:00Z",
+            },
+            {
+                "id": 987654321,
+                "topic": "Scheduled Meeting 2",
+                "type": 2,
+                "start_time": "2024-02-02T15:00:00Z",
+            },
+        ],
+    }
+
+    with patch.object(ZoomTools, "get_access_token", return_value="test_token"), patch("requests.get") as mock_get:
+        mock_get.return_value.json.return_value = mock_response
+        mock_get.return_value.raise_for_status = MagicMock()
+
+        result = zoom_tools.list_meetings(type="scheduled")
+        result_data = json.loads(result)
+
+        assert result_data["message"] == "Meetings retrieved successfully"
+        assert result_data["total_records"] == 2
+        assert len(result_data["meetings"]) == 2
+        assert result_data["meetings"][0]["id"] == 123456789
+        assert result_data["meetings"][1]["topic"] == "Scheduled Meeting 2"
+
+
+def test_get_meeting_recordings_success(zoom_tools):
+    """Test successful retrieval of meeting recordings"""
+    mock_response = {
+        "id": 123456789,
+        "uuid": "abcd1234",
+        "host_id": "host123",
+        "topic": "Recorded Meeting",
+        "start_time": "2024-02-01T10:00:00Z",
+        "duration": 60,
+        "total_size": 1000000,
+        "recording_count": 2,
+        "recording_files": [
+            {
+                "id": "rec1",
+                "meeting_id": "123456789",
+                "recording_type": "shared_screen_with_speaker_view",
+                "file_type": "MP4",
+                "file_size": 500000,
+            },
+            {
+                "id": "rec2",
+                "meeting_id": "123456789",
+                "recording_type": "audio_only",
+                "file_type": "M4A",
+                "file_size": 500000,
+            },
+        ],
+    }
+
+    with patch.object(ZoomTools, "get_access_token", return_value="test_token"), patch("requests.get") as mock_get:
+        mock_get.return_value.json.return_value = mock_response
+        mock_get.return_value.raise_for_status = MagicMock()
+
+        result = zoom_tools.get_meeting_recordings("123456789")
+        result_data = json.loads(result)
+
+        assert result_data["message"] == "Meeting recordings retrieved successfully"
+        assert result_data["meeting_id"] == "123456789"
+        assert result_data["recording_count"] == 2
+        assert len(result_data["recording_files"]) == 2
+        assert result_data["recording_files"][0]["recording_type"] == "shared_screen_with_speaker_view"
+        assert result_data["recording_files"][1]["recording_type"] == "audio_only"
+
+
+def test_delete_meeting_success(zoom_tools):
+    """Test successful meeting deletion"""
+    with patch.object(ZoomTools, "get_access_token", return_value="test_token"), patch(
+        "requests.delete"
+    ) as mock_delete:
+        mock_delete.return_value.status_code = 204
+        mock_delete.return_value.raise_for_status = MagicMock()
+
+        result = zoom_tools.delete_meeting("123456789")
+        result_data = json.loads(result)
+
+        assert result_data["message"] == "Meeting deleted successfully!"
+        assert result_data["meeting_id"] == "123456789"
+
+        # Verify the delete request
+        mock_delete.assert_called_once()
+        args, kwargs = mock_delete.call_args
+        assert args[0] == "https://api.zoom.us/v2/meetings/123456789"
+        assert kwargs["headers"]["Authorization"] == "Bearer test_token"
+
+
+@pytest.mark.parametrize(
+    "method_name,mock_func,error_message",
+    [
+        ("get_meeting", "requests.get", "Meeting not found"),
+        ("get_upcoming_meetings", "requests.get", "Failed to fetch upcoming meetings"),
+        ("list_meetings", "requests.get", "Failed to list meetings"),
+        ("get_meeting_recordings", "requests.get", "No recordings found"),
+        ("delete_meeting", "requests.delete", "Meeting deletion failed"),
+    ],
+)
+def test_api_methods_request_failure(zoom_tools, method_name, mock_func, error_message):
+    """Test API methods handle request failures gracefully"""
+    with patch.object(ZoomTools, "get_access_token", return_value="test_token"), patch(mock_func) as mock_request:
+        mock_request.side_effect = requests.RequestException(error_message)
+
+        method = getattr(zoom_tools, method_name)
+        if method_name == "delete_meeting":
+            result = method("123456789", schedule_for_reminder=True)
+        else:
+            result = method("123456789" if "meeting" in method_name else "me")
+
+        error_response = json.loads(result)
+        assert "error" in error_response
+        assert error_message in str(error_response["error"])
```

