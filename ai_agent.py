from llama_index.tools.mcp import McpToolSpec
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings

llm = Ollama(model="llama3.2", request_timeout=120.0)
Settings.llm = llm
SYSTEM_PROMPT = """
You are an expert SQL assistant that generates, explains, and safely executes SQL queries. 
Always validate instructions and confirm before running any query that modifies or deletes data. 
For each request, provide the SQL statement and a plain-language explanation. 
If information is missing or ambiguous, ask clarifying questions before proceeding.
"""


async def get_agent(tools: McpToolSpec):
    tools = await tools.to_tool_list_async()
    agent = FunctionAgent(
        name="Agent",
        description="An agent that can work with Our Database software.",
        tools=tools,
        llm=llm,
        system_prompt=SYSTEM_PROMPT,
    )
    return agent
