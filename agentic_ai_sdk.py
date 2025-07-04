agentic_ai_sdk/
├── agents/
│   └── base_agent.py
├── core/
│   ├── planner.py
│   ├── memory.py
│   ├── tools.py
│   └── llm.py
├── examples/
│   └── sample_agent.py
├── tests/
│   └── test_agent.py
├── __init__.py
├── config.py
├── constants.py
├── requirements.txt
├── README.md
└── setup.py

# base_agent.py
class BaseAgent:
    def __init__(self, planner, memory, tools):
        self.planner = planner
        self.memory = memory
        self.tools = tools

    def run(self, task):
        plan = self.planner.plan(task)
        for step in plan:
            result = self.tools.execute(step)
            self.memory.store(step, result)
        return result

# planner.py
class Planner:
    def plan(self, task):
        # Placeholder logic: split task into fake steps
        return [f"step: {task}"]

# memory.py
class Memory:
    def __init__(self):
        self.history = []

    def store(self, step, result):
        self.history.append({"step": step, "result": result})

# tools.py
class Tool:
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def run(self, *args, **kwargs):
        return self.func(*args, **kwargs)

class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, tool):
        self.tools[tool.name] = tool

    def execute(self, step):
        # Dummy execution
        return f"Executed: {step}"

# llm.py
class LLM:
    def __init__(self, provider):
        self.provider = provider

    def generate(self, prompt):
        return f"LLM response to: {prompt}"

# sample_agent.py
from agentic_ai_sdk.agents.base_agent import BaseAgent
from agentic_ai_sdk.core import planner, memory, tools

if __name__ == "__main__":
    p = planner.Planner()
    m = memory.Memory()
    t = tools.ToolRegistry()
    agent = BaseAgent(p, m, t)
    print(agent.run("Schedule a meeting"))

# test_agent.py
def test_basic_agent():
    from agentic_ai_sdk.agents.base_agent import BaseAgent
    from agentic_ai_sdk.core import planner, memory, tools
    
    agent = BaseAgent(planner.Planner(), memory.Memory(), tools.ToolRegistry())
    result = agent.run("Say hello")
    assert "Executed" in result

# requirements.txt
openai

# setup.py
from setuptools import setup, find_packages

setup(
    name="agentic_ai_sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["openai"],
)

# README.md
# Agentic AI SDK

A lightweight SDK to build agentic applications using LLMs.

## Features
- Agent runtime and planner
- Tool registry and execution
- In-memory context tracking

## Quickstart
```bash
pip install -e .
python examples/sample_agent.py
```

## License
MIT
