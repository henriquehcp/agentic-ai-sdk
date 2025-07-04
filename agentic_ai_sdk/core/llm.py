class LLM:
    def __init__(self, provider):
        self.provider = provider

    def generate(self, prompt):
        return f"LLM response to: {prompt}"
