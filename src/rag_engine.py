import sys
import os

# FIX: Windows ChromaDB crash fix
try:
    __import__('pysqlite3')
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError:
    pass

# --- IMPORTS ---
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.llms import Ollama

def load_pdf(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    loader = PyPDFLoader(file_path)
    return loader.load()

def create_vector_db(pages):
    print("Splitting text...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(pages)
    
    print("Creating Vector Database (Fast Mode)...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./data/vector_store"
    )
    print("Database created!")
    return vector_db

def ask_pdf(question):
    print(f"\n--- DEBUG LOG: Asking Llama-3 about: {question} ---")
    
    # Setup Brain & Database
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_db = Chroma(persist_directory="./data/vector_store", embedding_function=embeddings)
    llm = Ollama(model="llama3")
    
    # Search & Generate
    docs = vector_db.similarity_search(question, k=3)
    
    # DEBUG: Check if we found anything in the manual
    if not docs:
        print("--- DEBUG ERROR: No matching text found in database! ---")
        return "I could not find any information about that in the manual."
    
    context = "\n\n".join([doc.page_content for doc in docs])
    print(f"--- DEBUG: Found context length: {len(context)} characters ---")
    
    prompt = f"""
    You are a Senior Hardware Technician.
    MANUAL CONTENT:
    {context}
    
    USER QUESTION: 
    {question}
    
    ANSWER:
    """
    
    # Get response
    response = llm.invoke(prompt)
    print(f"--- DEBUG: Llama-3 Replied: {response}")
    
    return response