import os

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI


print(os.environ.get("SERPAPI_API_KEY"))
llm = OpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")