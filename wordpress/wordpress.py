from llama_index import GPTSimpleVectorIndex, download_loader
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain


def load_documents():
    WordpressReader = download_loader("WordpressReader")
    loader = WordpressReader(url="https://pjq.me", username="xxxx", password="my_password")
    documents = loader.load_data()
    langchain_documents = [d.to_langchain_format() for d in documents]

    return langchain_documents


def initialize_qa_chain():
    llm = OpenAI(temperature=0)
    qa_chain = load_qa_chain(llm)

    return qa_chain


def get_answer(qa_chain, langchain_documents, question):
    return qa_chain.run(input_documents=langchain_documents, question=question)


def main():
    print("Welcome to the ChatBot! Type 'quit' to exit.")
    langchain_documents = load_documents()
    qa_chain = initialize_qa_chain()

    while True:
        question = input("Please enter your question: ")
        if question.lower() == 'quit':
            break

        answer = get_answer(qa_chain, langchain_documents, question)
        print(f"Answer: {answer}")
        print("---------")


if __name__ == "__main__":
    main()
