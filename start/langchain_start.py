import os
import requests
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

# Create an OpenAI LLM instance
# llm = OpenAI(model_name="text-ada-001", n=2, best_of=2, session=session)
# llm = ChatOpenAI(model_name="gpt-3.5-turbo", n=2, best_of=2, session=session)
llm = OpenAI(model_name="text-ada-001", n=2, best_of=2)

# Generate text
joke = llm("Tell me a joke")
print(joke)

# Generate a complete response
llm_result = llm.generate(["Tell me a joke", "Tell me a poem"] * 15)

# Access generated responses
print(len(llm_result.generations))
print(llm_result.generations[0])
print(llm_result.generations[-1])
print(llm_result.llm_output)

# Estimate the number of tokens
tokens = llm.get_num_tokens("what a joke")
print(tokens)
