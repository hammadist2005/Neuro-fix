import streamlit as st
import os
import sys

# Allow importing from src folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.vision_engine import analyze_image
from src.rag_engine import ask_pdf

st.set_page_config(page_title="Neuro-fix", layout="wide")
st.title("Neuro-fix: AI Hardware Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Vision Input")
    img_file = st.camera_input("Scan Component")
    detected_part = None

    if img_file:
        with open("temp.jpg", "wb") as f:
            f.write(img_file.getbuffer())
        
        with st.spinner("Analyzing circuit..."):
            detected_part = analyze_image("temp.jpg")
        
        if detected_part:
            st.success(f"Detected: {detected_part}")
        else:
            st.warning("No component identified.")

with col2:
    st.header("Diagnostic Chat")
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Describe the issue..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Consulting manual..."):
                if detected_part:
                    full_query = f"I am looking at a {detected_part}. {prompt}"
                else:
                    full_query = prompt
                
                response = ask_pdf(full_query)
                final_answer = response["result"]
                st.markdown(final_answer)
        
        st.session_state.messages.append({"role": "assistant", "content": final_answer})