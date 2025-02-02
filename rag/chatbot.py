import os
from langchain import hub
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Fetch API keys from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
USER_AGENT = os.getenv("DefaultLangchainUserAgent")

if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API key")

# Initialize ChatOpenAI
llm = ChatOpenAI(model="gpt-4o", openai_api_key=OPENAI_API_KEY)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Define persistent vector store path
VECTORSTORE_PATH = os.path.join(BASE_DIR, "vectorstore")

content_path = os.path.join(BASE_DIR, "content.txt")
with open(content_path, "r", encoding="utf-8") as file:
    content = file.read()

# Process the content with LangChain modules
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_text(content)

# Check if vector store exists, otherwise create it
if not os.path.exists(VECTORSTORE_PATH):
    vectorstore = Chroma.from_texts(texts=splits, embedding=OpenAIEmbeddings(), persist_directory=VECTORSTORE_PATH)
else:
    vectorstore = Chroma(persist_directory=VECTORSTORE_PATH, embedding_function=OpenAIEmbeddings())

retriever = vectorstore.as_retriever(search_kwargs={"k": min(2, len(splits))})

# Load the prompt template
prompt = hub.pull("rlm/rag-prompt")

# Define RAG pipeline
rag_chain = (
    {"context": retriever | (lambda text: text), "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def get_response(query: str) -> str:
    """Fetches a response using the RAG pipeline and provides a fallback if needed."""
    try:
        response = rag_chain.invoke(query)
        
        # Fallback if response is too short
        if len(response.split()) < 6:
            response = llm.invoke(query).content

        return response.strip()
    except Exception:
        return "An error occurred while processing your request."

# Example usage
if __name__ == "__main__":
    query = "how much money has been saved?"
    print(get_response(query))
