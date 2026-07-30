from yutra.llm.client import LLMClient


class Brain:
    def __init__(self, llm: LLMClient):
        self.llm = llm
        

        
        


    def think(self, user_input: str) -> str:
        return self.llm.generate(user_input)

