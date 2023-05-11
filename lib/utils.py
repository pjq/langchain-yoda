from langchain.llms import OpenAI
import os
import requests


def createOpenAIWithProxy():
    proxy_url = os.environ.get('HTTP_PROXY') or os.environ.get('HTTPS_PROXY')
    # Custom session
    if proxy_url is None:
        print("set up you proxy here")

    print("proxy:" , proxy_url)
    session = requests.Session()

    # If a proxy is set, configure the session to use the proxy
    if proxy_url:
        proxies = {'http': proxy_url, 'https': proxy_url}
        session.proxies.update(proxies)

    # llm = OpenAI(session=session)
    llm = OpenAI()

    return llm

def getLlamaModel():

    import os
    return os.environ["MODEL"]

def getGpt4allModel():

    import os
    return os.environ["MODEL"]

def createLlama():
    from langchain.llms import LlamaCpp
    from langchain import PromptTemplate, LLMChain
    llm = LlamaCpp(model_path=getLlamaModel())

    return llm

def createLlamaEmbeddings():
    from langchain.embeddings import LlamaCppEmbeddings
    from langchain.llms import LlamaCpp
    from langchain import PromptTemplate, LLMChain
    llama = LlamaCppEmbeddings(model_path=getLlamaModel(), n_ctx=2048)

    return llama

def createGoogleSearch():
    import os
    # os.environ["GOOGLE_CSE_ID"] = ""
    # os.environ["GOOGLE_API_KEY"] = ""
    from langchain.utilities import GoogleSearchAPIWrapper
    search = GoogleSearchAPIWrapper()

    return search

def createGoogleSerper():
    from langchain.utilities import GoogleSerperAPIWrapper
    import os
    # os.environ["SERPER_API_KEY"] = ""
    search = GoogleSerperAPIWrapper()

    return search

def createBash():
    from langchain.utilities import BashProcess
    tool = BashProcess()

    return tool

def createWolfram():
    from langchain.utilities import WolframAlphaAPIWrapper
    tool = WolframAlphaAPIWrapper()
    # os.environ["WOLFRAM_ALPHA_APPID"] = ""

    return tool
def createOpenWeatherMap():
    from langchain.utilities import OpenWeatherMapAPIWrapper
    tool = OpenWeatherMapAPIWrapper()
    # os.environ["OPENWEATHERMAP_API_KEY"] = ""

    return tool
def createHuman():
    from langchain.tools.human import tool
    tool = tool.HumanInputRun()

    return tool
def createVisionCaption():
    from lib.vision_caption import VisionCaptionTool
    tool = VisionCaptionTool()

    return tool
def createVisionControl():
    from lib.vision_control import  VisionControl
    tool = VisionControl()

    return tool
