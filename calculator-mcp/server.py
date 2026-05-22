
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("calculator-mcp")


@mcp.tool()
def calculator(expression: str) -> dict:

    try:

        result = eval(expression)

        return {
            "success": True,
            "result": result
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


if __name__ == "__main__":

    mcp.run()

