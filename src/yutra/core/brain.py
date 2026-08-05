from yutra.llm.client import BaseLLM


class Brain:
    def __init__(self, llm: BaseLLM):
        self.llm = llm
        self.messages = []

    def think(self, user_input: str) -> str:
        message_that_going_to_add = {
            "role": "user",
            "content": user_input
        }
        self.messages.append(message_that_going_to_add)
        answer_of_llm =  self.llm.generate(self.messages)

        answer_that_going_to_add_to_memory = {
            "role": "assistant",
            "content": answer_of_llm
        }
        self.messages.append(answer_that_going_to_add_to_memory)
        return answer_of_llm






