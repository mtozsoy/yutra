from yutra.llm.base import BaseLLM


class LLMClient(BaseLLM):
    def generate(self, prompt: str) -> str:
        return f"LLM Cevabı : {prompt}"
