from yutra.llm.client import BaseLLM
from yutra.memory.conversation import ConversationMemory
from yutra.prompts.system import SYSTEM_PROMPT


class Brain:
    def __init__(self, llm: BaseLLM):
        self.llm = llm
        self.memory = ConversationMemory()
        self.memory.add("system",SYSTEM_PROMPT)
        

    def think(self, user_input: str) -> str:
        self.memory.add("user",user_input)

        messages = self.memory.get_messages()
        response = self.llm.generate(messages)

        self.memory.add("assistant",response)

        return response






