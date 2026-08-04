from yutra.llm.client import BaseLLM


class Brain:
    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def think(self, user_input: str) -> str:
        return self.llm.generate(user_input)
