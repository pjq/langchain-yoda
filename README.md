# LangChain-Yoda

LangChain-Yoda is a collection of various agents and tools built based on Langchain to explore the capabilities of 
- natural language processing using open-source libraries and APIs.
- kinds of tools and agents build by Langchain
- Embeddings and index capability

### Setup the KEYS

```shell
export GOOGLE_CSE_ID=""
export GOOGLE_API_KEY=""
export SERPER_API_KEY=""
export MODEL=""
```

### Install the dependencies
```shell
pip install -r requirements.txt
```

## File Structure
The repository has the following file structure:

```
LangChain/
├── agent/
│   ├── bashbot.py
│   ├── googlesearch.py
│   ├── googlesearch_chatbot.py
│   └── langchain_agent.py
├── gpt4all/
│   └── gpt4all.py
├── index/
│   ├── blog.txt
│   ├── langchain_index.py
│   └── state_of_the_union.txt
├── lib/
│   └── proxy.py
├── llama-cpp/
│   ├── llama.py
│   └── llama_embed.py
├── main.py
├── openai/
│   └── langchain_openai.py
├── requirements.txt
└── start/
    └── langchain_start.py
```

### Description of Directories and Files

#### agent/

The `agent/` directory contains various agents built for specific tasks in natural language processing, including a Bashbot that executes shell commands, a Googlesearch that provides search results from Google, and a Langchain Agent that performs various NLP-related tasks.

#### gpt4all/

The `gpt4all/` directory contains Python scripts for interacting with the OpenAI GPT-3 API. 

#### index/

The `index/` directory contains sample text files designed for language processing, including a blog post and a transcript of President Barack Obama's 2009 inaugural address. 

#### lib/

The `lib/` directory contains helper modules.

#### llama-cpp/

The `llama-cpp/` directory contains Python scripts that use the Llama Embeddings Module to perform NLP-related tasks.

#### openai/

The `openai/` directory contains Python scripts for interacting with the OpenAI GPT-3 API.

#### requirements.txt

`requirements.txt` contains a list of Python packages required to run the scripts in the repository.

#### start/

The `start/` directory contains Python scripts for launching the various agents and tools in LangChain.

## Getting Started

To get started with LangChain, clone the repository and install the required packages by running:

```
pip install -r requirements.txt
```

Then, navigate to the `start/` directory and choose one of the Python scripts to launch an agent or tool. For example, to launch the Langchain Agent, run:

```
python langchain_start.py
```

## License

The code in this repository is licensed under the MIT License. Please read the `LICENSE` file in the root directory for more information.


## OpenAI/ChatGPT
### GPT-4
- https://platform.openai.com/docs/models/gpt-4

### GPT Plugins
- https://openai.com/blog/chatgpt-plugins
- https://platform.openai.com/docs/plugins/examples
- https://github.com/openai/chatgpt-retrieval-plugin

## How to build you own ChatGPT App
- https://github.com/pjq/chitchat

## LLM
### gpt4all
- https://github.com/nomic-ai/gpt4all

### Alpaca.cpp
- https://github.com/antimatter15/alpaca.cpp
### llama.cpp
- https://github.com/ggerganov/llama.cpp

## langchain
- https://python.langchain.com/en/latest/index.html

### Tools
- https://python.langchain.com/en/latest/modules/agents/tools.html

### Agents
- https://python.langchain.com/en/latest/modules/agents/agents.html


## Prompts
- https://github.com/rockbenben/ChatGPT-Shortcut
- https://www.explainthis.io/zh-hans/chatgpt

## Auto fix bug in CI/CD
- https://twitter.com/calvinhoenes/status/1642441789033578498

## Refer
- https://github.com/hwchase17/chat-your-data/
- https://python.langchain.com/en/latest/index.html
- https://blog.langchain.dev/tutorial-chatgpt-over-your-data/
- https://github.com/f/awesome-chatgpt-prompts
- https://blog.lastmileai.dev/using-openais-retrieval-plugin-with-llama-d2e0b6732f14

