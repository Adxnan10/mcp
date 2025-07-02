from mcp_client import mcp_tools
from ai_agent import get_agent
from llama_index.core.workflow import Context
from handle_user_message import handle_user_message
import asyncio


async def main():
    # get the agent
    agent = await get_agent(mcp_tools)
    # create the agent context
    agent_context = Context(agent)
    # Run the agent!
    while True:
        user_input = input("Enter your message: ")
        if user_input == "exit":
            break
        print("User: ", user_input)
        response = await handle_user_message(user_input, agent, agent_context, verbose=True)
        print("Agent: ", response)

if __name__ == "__main__":
    asyncio.run(main())