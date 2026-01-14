import streamlit as st
import os
import sys

# Add the project root to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.vision_engine import analyze_image
from src.rag_engine import ask_pdf

st.set_page_config(page_title="Neuro-fix", layout="wide")
st.title("Neuro-fix: AI Hardware Assistant")

# --- SESSION STATE SETUP ---
# We use this to remember the "Auto-Diagnose" click
if 'auto_query' not in st.session_state:
    st.session_state.auto_query = None

col1, col2 = st.columns(2)

# --- LEFT COLUMN: VISION ---
with col1:
    st.header("Vision Input")
    picture = st.camera_input("Scan Component")
    
    if picture:
        # Save temp image
        with open("temp.jpg", "wb") as f:
            f.write(picture.getbuffer())
        
        st.write("Analyzing...")
        try:
            detected_object = analyze_image("temp.jpg")
            st.success(f"Detected: {detected_object}")
            
            # THE NEW FEATURE: "Diagnose" Button
            # Only show if we actually found something
            if detected_object and detected_object != "None":
                if st.button(f"Diagnose {detected_object}"):
                    st.session_state.auto_query = f"How do I troubleshoot or replace the {detected_object}?"
                    st.rerun() # Refresh to send the query
            else:
                st.warning("Try placing the object flat on a table for better detection.")
                
        except Exception as e:
            st.error(f"Vision Error: {e}")

# --- RIGHT COLUMN: CHAT ---
with col2:
    st.header("Diagnostic Chat")
    
    # 1. Check if the button triggered a query
    if st.session_state.auto_query:
        user_query = st.session_state.auto_query
        # Clear it so it doesn't loop
        st.session_state.auto_query = None
    else:
        # Otherwise, wait for typing
        user_query = st.chat_input("Describe the issue...")
    
    if user_query:
        # Show the User's message
        with st.chat_message("user"):
            st.write(user_query)
            
        # Get the Answer
        with st.chat_message("assistant"):
            with st.spinner("Analyzing Manual..."):
                try:
                    response = ask_pdf(user_query)
                    st.write(response)
                except Exception as e:
                    st.error(f"An error occurred: {e}")