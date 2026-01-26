import streamlit as st
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.fast_engine import ask_fast_ai, ask_gemini_vision
from src.vision_engine import analyze_image

from src.safety_guard import check_safety
from src.market_agent import check_czone_price
from src.hive_mind import search_hive

st.set_page_config(page_title="Neuro-fix", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #0e1117; color: #ffffff; }
        div.stButton > button { background-color: #00ADB5; color: white; border-radius: 8px; border: none; padding: 0.5rem 1rem; }
        div.stButton > button:hover { background-color: #00FFF5; color: black; }
        .status-box { padding: 15px; border-radius: 10px; margin-bottom: 20px; font-weight: bold; }
        .healthy { background-color: #1b5e20; border: 1px solid #4caf50; color: #e8f5e9; }
        .danger { background-color: #b71c1c; border: 1px solid #ef5350; color: #ffebee; }
    </style>
""", unsafe_allow_html=True)

st.title("Neuro-fix: AI Hardware Assistant")

if 'last_analyzed_image' not in st.session_state:
    st.session_state.last_analyzed_image = None
if 'cached_result' not in st.session_state:
    st.session_state.cached_result = (None, None)
if 'auto_query' not in st.session_state:
    st.session_state.auto_query = None

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.header("Visual Grounding")
    picture = st.camera_input("Scan Component")
    
    if picture:
        img_bytes = picture.getvalue()
        
        if img_bytes != st.session_state.last_analyzed_image:
            with st.spinner("Analyzing..."):
                detected_object, damage_status = analyze_image(picture) 

                st.session_state.last_analyzed_image = img_bytes
                st.session_state.cached_result = (detected_object, damage_status)
        
        detected_object, damage_status = st.session_state.cached_result
        
        st.image(picture, caption=f"Detected: {detected_object}", use_container_width=True)
        
        if damage_status:
            if "Error" in damage_status:
                 st.warning("⚠️ Traffic High. Click 'Clear photo' and try again in a moment.")
            elif "Healthy" in damage_status:
                st.markdown(f"<div class='status-box healthy'>✅ {damage_status}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='status-box danger'>⚠️ {damage_status}</div>", unsafe_allow_html=True)

            if "Error" not in damage_status and detected_object != "None":
                if st.button("Diagnose & Fix Issue", use_container_width=True):
                    st.session_state.auto_query = f"How do I fix {detected_object} with status: {damage_status}?"
                    st.rerun()

with col2:
    st.header("Neural Logic Core")
    if st.session_state.auto_query:
        user_query = st.session_state.auto_query
        st.session_state.auto_query = None
    else:
        user_query = st.chat_input("Ask about hardware...")
    
    if user_query:
        st.chat_message("user").write(user_query)
        
        if any(w in user_query.lower() for w in ["price", "buy", "cost"]):
            with st.spinner("Checking Market Prices..."):
                target = "RAM" if "ram" in user_query.lower() else "Hardware"
                market_data = check_czone_price(target)
                if market_data['found']:
                    st.info(f"💰 **{market_data['title']}**: {market_data['price']}")
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = ask_fast_ai(user_query)
                st.write(response)