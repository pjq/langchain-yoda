import os
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
import lib.utils as proxy

class ChatBot:
    def __init__(self):
        # Set up tools
        search = proxy.createGoogleSerper()
        bash = proxy.createBash()
        wolfram = proxy.createWolfram()
        human = proxy.createHuman()
        weather = proxy.createOpenWeatherMap()
        vision_caption = proxy.createVisionCaption()
        vision_control = proxy.createVisionControl()

        self.tools = [
            Tool(
                name="Google Search",
                func=search.run,
                description="Useful for answering questions about current events or the current state of the world. The input should be a single search term."
            ),
            Tool(
                name="Wolfram",
                func=wolfram.run,
                description="Computational knowledge engine."
            ),
            Tool(
                name="Human",
                func=human.run,
                description="Human agent for difficult questions."
            ),
            Tool(
                name="Weather",
                func=weather.run,
                description="Provides weather information."
            ),
            vision_caption,
            vision_control,
            Tool(
                name="Bash Process",
                func=bash.run,
                description="Useful for controlling or getting information from the current system."
            )
        ]

        # Set up the chatbot
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self.llm = ChatOpenAI(temperature=0)
        self.agent_chain = initialize_agent(self.tools, self.llm, agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, verbose=True, memory=self.memory)

    def start_chat(self):
        # Start chatting with the user
        print('Bot: Hello! How can I assist you today?')
        while True:
            try:
                user_input = input('You: ')
                if user_input.lower() in ['exit', 'bye', 'quit']:
                    print('Bot: Goodbye!')
                    break
                response = self.agent_chain.run(user_input)
                print(f'Bot: {response}')
            except Exception as e:
                print(f'An error occurred: {e}')

if __name__ == '__main__':
    bot = ChatBot()
    bot.start_chat()
