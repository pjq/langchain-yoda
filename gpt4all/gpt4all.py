from langchain.llms import LlamaCpp
from langchain.llms import GPT4All
from langchain import PromptTemplate, LLMChain
import lib.utils as proxy

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = GPT4All(model=proxy.getGpt4allModel())
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Function to get user input through terminal or other means
def get_user_input():
    return input("What would you like to ask? ")

# Run the chatbot
while True:
    try:
        # Get user input
        user_input = get_user_input()

        # Stop the chatbot if user types "quit"
        if user_input.lower() == "quit":
            break

        # Generate response using LLMChain
        response = llm_chain.run(user_input)

        # Print the bot's response
        print(response)

    except Exception as e:
        print(f"Error: {e}")
