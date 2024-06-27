import os
from langchain import hub
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI



openai_api_key = os.environ.get("OPENAI_API_KEY")
user_agent = os.environ.get("DefaultLangchainUserAgent")


# Initialize ChatOpenAI with your API key
llm = ChatOpenAI(model="gpt-3.5-turbo-0125")

# Read content from content.txt
with open('rag/content.txt', 'r') as file:
    content = file.read()

# Process the content using langchain modules
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_text(content)
vectorstore = Chroma.from_texts(texts=splits, embedding=OpenAIEmbeddings())

# Retrieve and generate using the relevant snippets of the content
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")

def format_text(text):
    return text

rag_chain = (
    {"context": retriever | format_text, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def get_response(query):
    response = rag_chain.invoke(query)

    # If the response is empty or not satisfactory, fallback to a general query
    if len(response.split())<6:
        fallback_query = query
        response = llm.invoke(fallback_query)
        response = response.content

    return response


