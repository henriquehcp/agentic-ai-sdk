def test_basic_agent():
    from agentic_ai_sdk.agents.base_agent import BaseAgent
    from agentic_ai_sdk.core import planner, memory, tools
    
    agent = BaseAgent(planner.Planner(), memory.Memory(), tools.ToolRegistry())
    result = agent.run("Say hello")
    assert "Executed" in result
