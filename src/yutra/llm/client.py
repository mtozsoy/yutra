from yutra.llm.base import BaseLLM


class LLMClient(BaseLLM):
    def generate(self, messages : list[dict]) -> str:
        return f"LLM Cevabı : {messages}"
