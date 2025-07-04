from agentic_ai_sdk.agents.base_agent import BaseAgent
from agentic_ai_sdk.core import planner, memory, tools

if __name__ == "__main__":
    p = planner.Planner()
    m = memory.Memory()
    t = tools.ToolRegistry()
    agent = BaseAgent(p, m, t)
    print(agent.run("Schedule a meeting"))
