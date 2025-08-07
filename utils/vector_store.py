from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize embedding model
embedding_model = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

def create_vector_store(chunks):
    """
    Converts text chunks to embeddings and stores them in a FAISS index.
    """
    vector_store = FAISS.from_texts(chunks, embedding_model)
    return vector_store

def retrieve_relevant_chunks(query, vector_store, k=4):
    """
    Retrieves top-k most relevant chunks from the vector store based on the query.
    """
    docs = vector_store.similarity_search(query, k=k)
    return [doc.page_content for doc in docs]
