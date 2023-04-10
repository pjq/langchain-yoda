from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
import lib.utils as proxy
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = LlamaCpp(model_path= proxy.getLlamaModel())
llm_chain = LLMChain(prompt=prompt, llm=llm)
question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

result = llm_chain.run(question)
print(result)