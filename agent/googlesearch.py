from langchain.utilities import GoogleSearchAPIWrapper
import lib.utils as proxy
search = proxy.createGoogleSearch()
result = search.results("Obama", 5)
# result = search.run("Obama's first name?")
print(result)