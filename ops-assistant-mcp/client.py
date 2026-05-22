import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()

            print("\n✅ Connected to MCP Server\n")

            # List tools
            tools = await session.list_tools()
            print("📦 Tools:")
            for t in tools.tools:
                print("-", t.name)

            # Call add_note
            res = await session.call_tool(
                "add_note",
                {
                    "title": "MCP Test",
                    "content": "Client working fine 🚀"
                }
            )
            print("\n📝 add_note result:", res)

            # Call get_notes
            res = await session.call_tool("get_notes", {})
            print("\n📚 get_notes:", res)


if __name__ == "__main__":
    asyncio.run(main())