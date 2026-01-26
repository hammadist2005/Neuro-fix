import streamlit as st
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.vision_engine import analyze_image
from src.fast_engine import ask_fast_ai
from src.safety_guard import check_safety
from src.market_agent import check_czone_price
from src.hive_mind import search_hive

st.set_page_config(
    page_title="Neuro-fix", 
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
        h1 { font-size: 3rem !important; font-weight: 800; color: #fff; }
        .danger-box { border: 2px solid #ff4b4b; background-color: #2d0f0f; padding: 15px; border-radius: 8px; color: #ff4b4b; font-weight: bold; margin-bottom: 15px; }
        .hive-box { border: 1px solid #00FF41; background-color: #001a05; padding: 15px; border-radius: 8px; color: #00FF41; margin-bottom: 15px; }
        .market-box { border: 1px solid #3a7bd5; background-color: #0d1b2a; padding: 15px; border-radius: 8px; color: #e0e0e0; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=50)
    st.markdown("## Neuro-fix")
    st.caption("v0.3 Enterprise Edition")

st.title("Neuro-fix: AI Hardware Assistant")

if 'auto_query' not in st.session_state:
    st.session_state.auto_query = None
if 'last_analyzed_image' not in st.session_state:
    st.session_state.last_analyzed_image = None
if 'cached_detected_object' not in st.session_state:
    st.session_state.cached_detected_object = None
if 'cached_damage_status' not in st.session_state:
    st.session_state.cached_damage_status = None

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.header("Visual Grounding")
    picture = st.camera_input("Scan Hardware")
    
    if picture:
        img_bytes = picture.getvalue()
        
        if img_bytes != st.session_state.last_analyzed_image:
            with open("temp.jpg", "wb") as f:
                f.write(img_bytes)
            
            with st.spinner("Scanning for physical damage..."):
                detected_object, damage_status = analyze_image("temp.jpg")
                
                st.session_state.last_analyzed_image = img_bytes
                st.session_state.cached_detected_object = detected_object
                st.session_state.cached_damage_status = damage_status
        
        detected_object = st.session_state.cached_detected_object
        damage_status = st.session_state.cached_damage_status
        
        if os.path.exists("annotated_temp.jpg"):
            st.image("annotated_temp.jpg", caption=f"Identified: {detected_object}", use_container_width=True)
        elif os.path.exists("temp.jpg"):
            st.image("temp.jpg", caption=f"Identified: {detected_object}", use_container_width=True)
        else:
            st.image(picture, caption=f"Identified: {detected_object}", use_container_width=True)
        
        if "Healthy" in damage_status:
            st.success(f"✅ {damage_status}")
        elif "Critical" in damage_status or "Burn" in damage_status or "damage" in damage_status:
            st.error(f"⚠️ {damage_status}")
            st.markdown(f"""
                <a href="https://www.google.com/maps/search/computer+repair+near+me" target="_blank">
                    <button style='background-color:#d9534f; color:white; width:100%; padding:10px; border:none; border-radius:4px; cursor:pointer; font-weight:bold;'>
                        🚑 Critical Damage Detected - Find Repair Shop
                    </button>
                </a>
            """, unsafe_allow_html=True)
        else:
            st.info(f"ℹ️ {damage_status}")
            
        if detected_object and detected_object != "None":
            if st.button(f"Diagnose {detected_object}", use_container_width=True):
                st.session_state.auto_query = f"How do I troubleshoot or replace the {detected_object}?"
                st.rerun()

with col2:
    st.header("Neural Logic Core")
    
    if st.session_state.auto_query:
        user_query = st.session_state.auto_query
        st.session_state.auto_query = None
    else:
        user_query = st.chat_input("Describe the issue...")
    
    if user_query:
        st.chat_message("user").write(user_query)
        
        is_safe, warning_msg = check_safety(user_query)
        
        if not is_safe:
            st.markdown(f"<div class='danger-box'>{warning_msg}</div>", unsafe_allow_html=True)
        else:
            market_keywords = ["buy", "price", "cost", "new", "replace", "upgrade", "purchase"]
            if any(x in user_query.lower() for x in market_keywords):
                with st.spinner("Checking Karachi Prices..."):
                    target_component = "Hardware"
                    if "ram" in user_query.lower(): target_component = "ram"
                    elif "ssd" in user_query.lower(): target_component = "ssd"
                    elif "nvme" in user_query.lower(): target_component = "nvme"
                    elif "mouse" in user_query.lower(): target_component = "mouse"
                    elif "gpu" in user_query.lower(): target_component = "gpu"
                    
                    market_data = check_czone_price(target_component)
                    
                    if market_data['found']:
                        st.markdown(f"""
                            <div class='market-box'>
                                <strong>🛒 PROCUREMENT AGENT ({market_data['source']})</strong><br>
                                Item: {market_data['title']}<br>
                                Price: <span style='color: #00d2ff'>{market_data['price']}</span><br>
                                <a href='{market_data['link']}' target='_blank' style='color: #fff; text-decoration: underline;'>View Listing</a>
                            </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.caption(f"No instant price found for '{target_component}'. Checking live...")

            hive_result = search_hive(user_query)
            if hive_result:
                st.markdown(f"<div class='hive-box'><strong>VERIFIED FIX FOUND:</strong><br>{hive_result}</div>", unsafe_allow_html=True)
            
            with st.chat_message("assistant"):
                with st.spinner("Consulting Neural Cloud..."):
                    try:
                        response = ask_fast_ai(user_query)
                        st.write(response)     
                    except Exception as e:
                        st.error(f"System Error: {e}")