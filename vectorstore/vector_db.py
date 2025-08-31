from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from typing import List
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


PERSIST_DIR = "./chroma_db"

def get_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)

def store_documents(documents: List[Document]):
    db = get_vectorstore()
    db.add_documents(documents)
    db.persist()
    return db

def get_retriever():

    db = get_vectorstore()
    return db.as_retriever(search_kwargs={"k": 5})
