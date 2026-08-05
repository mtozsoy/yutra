from ollama import chat


class OllamaClient():
    def generate(self, messages: list[dict]) -> str:
        response = chat(
            model = "qwen3:4b",
            messages = messages,

        )
        
        return response.message.content
