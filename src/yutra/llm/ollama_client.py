from ollama import chat


class OllamaClient():
    def generate(self, prompt: str) -> str:
        response = chat(
            model = "qwen3:4b",
            messages = [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],    

        )
        
        return response.message.content
