from langchain.embeddings import LlamaCppEmbeddings
import lib.utils as proxy

llama = LlamaCppEmbeddings(model_path=proxy.getLlamaModel())
text = "This is a test document."
query_result = llama.embed_query(text)
doc_result = llama.embed_documents([text])
print(query_result)
print(doc_result)
