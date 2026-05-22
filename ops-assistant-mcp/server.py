from mcp.server.fastmcp import FastMCP
from tools.notes import new_notes, fetch_notes
from tools.reminders import fetch_reminders
from tools.reminders import create_reminder
from tools.weather import fetch_weather



# ==================================================
# CREATE MCP SERVER
# ==================================================
mcp = FastMCP("ops-assistant-mcp")

# -----------------------------
# 1. NOTES TOOL
# -----------------------------
@mcp.tool()
def add_note(title: str, content: str):
    return new_notes(title, content)

@mcp.tool()
def get_notes():
    """Fetch all notes"""
    return fetch_notes()

# -----------------------------
# 2. REMINDERS TOOL
# -----------------------------
@mcp.tool()
def add_reminder(task: str, time: str):
    return create_reminder(task, time)


@mcp.tool()
def get_reminders() :
    """Fetch all reminders"""
    return fetch_reminders()



# -----------------------------
# 4. WEATHER TOOL (mock fun)
# -----------------------------
@mcp.tool()
def get_weather(city: str):
    return fetch_weather(city)

# ==================================================
# START SERVER
# ==================================================
if __name__ == "__main__":

    mcp.run()

