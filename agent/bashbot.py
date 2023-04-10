from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
import lib.utils as proxy

# Set up tools
search = proxy.createBash()
tools = [
    Tool(
        name="Bash Process",
        func=search.run,
        description="useful for when you need to control or get the information from the current system"
    )
]

# Set up the chatbot
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
llm = ChatOpenAI(temperature=0)
agent_chain = initialize_agent(tools, llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, verbose=False, memory=memory)

# Start chatting with the user
print('Bot: Hello! How can I assist you today?')
while True:
    user_input = input('You: ')
    if user_input.lower() in ['exit', 'bye', 'quit']:
        print('Bot: Goodbye!')
        break
    response = agent_chain.run(user_input)
    # print(f'Bot: {response["action_input"]}')
    print(f'Bot: {response}')
