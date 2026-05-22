# 📄 Scope Document — Calculator MCP Server

## 🎯 Objective

Build the first standalone MCP server for Astra using a Calculator Tool.

This MCP server will:

* expose calculator functionality through MCP
* validate Astra ↔ MCP integration
* establish reusable MCP architecture patterns
* serve as the foundation for future MCP tools

---

# 🚀 Problem Statement

Currently Astra tools are directly invoked internally.

Example:

```python
calculator("2 + 2")
```

Problems:

* tightly coupled architecture
* tools cannot be independently deployed
* no remote tool execution
* difficult extensibility
* no MCP compatibility

---

# ✅ Proposed Solution

Create a standalone Calculator MCP Server using:

* MCP SDK
* FastMCP
* tool registration
* remote invocation

---

# 🧠 Target Architecture

```text
Astra Core
     ↓
MCP Client
     ↓
Calculator MCP Server
     ↓
Calculator Tool
```

---

# 📁 Project Structure

```text
astra-mcp-servers/
│
├── calculator-mcp/
│   ├── server.py
│   ├── requirements.txt
│   └── README.md
```

---

# 📦 Required Installations

## MCP SDK

```bash
pip install mcp
```

## MCP CLI Tools (Optional)

```bash
pip install "mcp[cli]"
```

---

# 🔧 Functional Requirements

## ✅ MCP Server

The system must expose a standalone MCP server.

---

## ✅ Calculator Tool Registration

The calculator tool must be registered using MCP decorators.

---

## ✅ Expression Evaluation

The tool must accept mathematical expressions.

Example:

```text
2 + 2
10 * 5
(5 + 2) * 3
```

---

## ✅ JSON Response

The server must return structured JSON responses.

Success Example:

```json
{
  "success": true,
  "expression": "2+2",
  "result": 4
}
```

Failure Example:

```json
{
  "success": false,
  "error": "division by zero"
}
```

---

# 🔥 Non-Functional Requirements

| Requirement     | Goal                           |
| --------------- | ------------------------------ |
| Extensibility   | Easy future tool additions     |
| Isolation       | Independent deployment         |
| Reusability     | Tool usable by multiple agents |
| Maintainability | Separate MCP repository        |
| Compatibility   | MCP standard compliance        |

---

# 🧠 Technical Design

## MCP Framework

Use:

```python
FastMCP
```

---

## Tool Registration

Use:

```python
@mcp.tool()
```

decorator for tool exposure.

---

## Transport Layer

Initial version will use:

* local stdio transport

Future versions may support:

* HTTP
* WebSocket
* SSE

---

# 🚀 Initial Scope Limitations

The first version will intentionally remain simple.

---

## ❌ No Authentication

---

## ❌ No Tool Discovery Metadata Customization

---

## ❌ No Async Execution

---

## ❌ No Distributed Deployment

---

## ❌ No Safe Expression Sandbox

Initial implementation may use:

```python
eval()
```

for simplicity.

Future versions will replace this with:

* AST parser
* sandboxed execution
* secure evaluator

---

# 🧪 Testing Scope

| Test               | Expected             |
| ------------------ | -------------------- |
| Valid expression   | correct result       |
| Invalid expression | graceful error       |
| MCP startup        | server boots         |
| MCP tool discovery | calculator visible   |
| Remote invocation  | successful execution |

---

# 🚀 Deliverables

## 📁 calculator-mcp/server.py

Standalone MCP server.

---

## 📁 calculator-mcp/requirements.txt

Dependency management.

---

## 📁 calculator-mcp/README.md

Setup and execution instructions.

---

# 📈 Expected Outcome

Astra gains its first:

* remotely callable tool
* MCP-compatible service
* distributed tool architecture

---

# 🏁 Final Goal

Transform Astra from:

```text
Monolithic Agent System
```

into:

```text
Distributed MCP-Based AI Platform
```
