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
