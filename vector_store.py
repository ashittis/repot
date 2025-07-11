from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


def create_vectorstore(documents):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_documents(documents, embeddings)
