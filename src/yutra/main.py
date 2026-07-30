from yutra.core.brain import Brain
from yutra.llm.client import LLMClient


def main():
   llm = LLMClient()
   brain = Brain(llm)


   while True:
       user_input = input("You: ")

       if user_input.lower() in ("exit","quit"):
           break

       response = brain.think(user_input=user_input)
       print(f"Yutra: {response}")
       


if __name__ == "__main__":
    main()
