import sys
try:
    __import__('pysqlite3')
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError:
    pass

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

def load_pdf(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    loader = PyPDFLoader(file_path)
    return loader.load()

def create_vector_db(pages):
    print("Splitting text...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(pages)
    
    print("Creating Vector Database...")
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=OllamaEmbeddings(model="llama3"),
        persist_directory="./data/vector_store"
    )
    print("Database created!")
    return vector_db

def ask_pdf(question):
    embedding_function = OllamaEmbeddings(model="llama3")
    vector_db = Chroma(persist_directory="./data/vector_store", embedding_function=embedding_function)
    
    llm = Ollama(model="llama3")
    
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)
    
    return qa_chain.invoke({"query": question})