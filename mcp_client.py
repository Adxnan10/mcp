from llama_index.tools.mcp import BasicMCPClient, McpToolSpec

mcp_client = BasicMCPClient("http://127.0.0.1:8000/sse")
mcp_tools = McpToolSpec(client=mcp_client)


def print_tools():
    tools = mcp_tools.to_tool_list()
    for tool in tools:
        print(tool.metadata.name, tool.metadata.description)


if __name__ == "__main__":
    print_tools()
