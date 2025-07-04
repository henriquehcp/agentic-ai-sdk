# 🧠 Agentic AI SDK

A lightweight and modular SDK to build **Agentic AI applications** — agents that think, plan, use tools, and reason with LLMs.

## 🚀 Features

- 🧩 Modular agent architecture (Planner, Memory, Tools, LLM)
- 🛠️ Dynamic tool registration and execution
- 🧠 Basic reasoning loop (ReAct-style planning)
- 🧪 Easy to test, extend, and integrate

## 📦 Project Structure

```
agentic_ai_sdk/
├── agents/        # Agent base class and orchestration
├── core/          # Planner, Memory, Tools, LLM interface
├── examples/      # Sample agents and use cases
├── tests/         # Unit tests
```

## 🔧 Installation

```bash
git clone https://github.com/henriquehcp/agentic-ai-sdk.git
cd agentic-ai-sdk
pip install -e .
```

## ⚡ Quickstart

```bash
python examples/sample_agent.py
```

Sample output:

```
Executed: step: Schedule a meeting
```

## 🔨 Defining a Tool

```python
from agentic_ai_sdk.core.tools import Tool

def greet(name):
    return f"Hello, {name}!"

tool = Tool(name="greet", func=greet)
tool_registry.register(tool)
```

## 🧠 Agent Lifecycle

1. **Planner** breaks down the task
2. **Agent** executes steps with registered tools
3. **Memory** stores results
4. **LLM** (optional) enhances reasoning and planning

## 🧪 Running Tests

```bash
pytest tests/
```

## 📚 Roadmap Ideas

- [ ] LLM-backed planner integration (OpenAI, Claude, etc.)
- [ ] Tool introspection with function-calling
- [ ] Vector memory support
- [ ] Multi-agent collaboration

## 📄 License

MIT

## 👨‍💻 Maintainer

Built by [@henriquehcp](https://github.com/YOUR_USERNAME)
