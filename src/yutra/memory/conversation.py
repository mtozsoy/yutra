class ConversationMemory:
    def __init__(self):
        self.messages = []


    def add(self,role : str, content: str) -> None:
        self.messages.append({
            "role": role,
            "content": content
        })

    def get_messages(self) -> list[dict]:
        return self.messages
