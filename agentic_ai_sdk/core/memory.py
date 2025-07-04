class Memory:
    def __init__(self):
        self.history = []

    def store(self, step, result):
        self.history.append({"step": step, "result": result})
