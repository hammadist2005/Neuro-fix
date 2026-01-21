import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from rag_engine import load_pdf, create_vector_db

pdf_path = "data/manuals/manual.pdf" 

if os.path.exists(pdf_path):
    print(f"Loading {pdf_path}...")
    pages = load_pdf(pdf_path)
    
    print("Creating database...")
    create_vector_db(pages)
    
    print("SUCCESS: Database is ready!")
else:
    print(f"ERROR: Could not find file at {pdf_path}")