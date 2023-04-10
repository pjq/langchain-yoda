# Import necessary libraries
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
import lib.utils as proxy

# Define a template message for the chatbot to display
template = """Question: {question}

Answer: Let's think step by step."""

# Create a PromptTemplate object using the template message and the variable 'question'
prompt = PromptTemplate(template=template, input_variables=["question"])

# Create an OpenAI object with proxy support to call the language API
llm = proxy.createOpenAIWithProxy()

# Create an LLMChain object with the prompt and OpenAI object
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Define the chatbot's response to the user's input
def chatbot_response(input_text):
    # Use the LLMChain object to generate a response to the user's input
    response = llm_chain.run(input_text)
    return response

# Loop for user input and generating responses
while True:
    user_input = input("What question do you have? ")
    response = chatbot_response(user_input)
    print(response)
