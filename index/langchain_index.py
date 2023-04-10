from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import lib.utils as proxy

# specify the document loader to use
loader = TextLoader('blog.txt', encoding="utf-8")

# create the vectorstore index
# index = VectorstoreIndexCreator(vectorstore_cls=Chroma, embedding=OpenAIEmbeddings(),
#                                 text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)).from_loaders([loader])
# index = VectorstoreIndexCreator().from_loaders([loader])
index = VectorstoreIndexCreator(vectorstore_cls=Chroma, embedding=proxy.createLlamaEmbeddings(),
                                text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)).from_loaders([loader])

# create a retriever from the index
retriever = index.vectorstore.as_retriever(search_kwargs={"k": 1})

# create a question answering chain
# llm = proxy.createOpenAIWithProxy()
llm = proxy.createLlama()
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
# qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever(search_kwargs={"k": 1}))
# index.query("What's talking about")

# chat with the user
while True:
    question = input('You: ')
    if question.lower() == 'bye':
        break
    answer = qa.run(question)
    print('Bot:', answer)
