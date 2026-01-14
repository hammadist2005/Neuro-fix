import streamlit as st
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.vision_engine import analyze_image
from src.rag_engine import ask_pdf

st.set_page_config(
    page_title="Neuro-fix", 
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;
        }

        h1 {
            font-size: 3rem !important;
            font-weight: 800 !important;
            color: #FFFFFF !important;
            margin-bottom: 1.5rem !important;
            letter-spacing: -1px;
        }

        h2 {
            font-size: 1.6rem !important;
            font-weight: 600 !important;
            color: #E0E0E0 !important;
            border-bottom: 2px solid #333;
            padding-bottom: 0.5rem;
            margin-bottom: 1rem !important;
        }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=50)
    st.markdown("## Neuro-fix")
    st.markdown("Automated Hardware Diagnostics powered by Computer Vision & RAG.")
    
    st.markdown("---")
    
    st.markdown("### Tech Stack")
    st.code("Python 3.9+", language="text")
    st.code("YOLOv8 (Vision)", language="text")
    st.code("Llama-3 (Logic)", language="text")
    
    st.markdown("---")
    
    st.markdown("### Developer")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Repo-white?logo=github)](https://github.com/hammadist2005)")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/hammad-bin-tahir-1a3316264)")
    
    st.markdown("---")
    st.caption("v0.2 Engineering Prototype")

st.title("Neuro-fix: AI Hardware Assistant")

if 'auto_query' not in st.session_state:
    st.session_state.auto_query = None

col1, col2 = st.columns([1, 1], gap="large") 

with col1:
    st.header("Vision Input")
    picture = st.camera_input("Scan Component")
    
    if picture:
        with open("temp.jpg", "wb") as f:
            f.write(picture.getbuffer())
        
        st.write("") 
        
        with st.spinner("Analyzing image..."):
            try:
                detected_object = analyze_image("temp.jpg")
                
                if detected_object and detected_object != "None":
                    st.success(f"**Detected:** {detected_object}")
                    
                    st.write("")
                    
                    if st.button(f"Diagnose {detected_object}", use_container_width=True):
                        st.session_state.auto_query = f"How do I troubleshoot or replace the {detected_object}?"
                        st.rerun()
                else:
                    st.warning("No object detected. Try moving closer.")
            except Exception as e:
                st.error(f"Error: {e}")

with col2:
    st.header("Diagnostic Chat")
    
    if st.session_state.auto_query:
        user_query = st.session_state.auto_query
        st.session_state.auto_query = None
    else:
        user_query = st.chat_input("Describe the issue...")
    
    if user_query:
        with st.chat_message("user"):
            st.write(user_query)
            
        with st.chat_message("assistant"):
            with st.spinner("Searching manuals..."):
                try:
                    response = ask_pdf(user_query)
                    st.write(response)
                except Exception as e:
                    st.error(f"Error: {e}")