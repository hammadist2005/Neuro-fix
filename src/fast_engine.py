import os
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    import streamlit as st
    try:
        api_key = st.secrets["GOOGLE_API_KEY"]
    except:
        pass

genai.configure(api_key=api_key)
MODEL_NAME = "gemini-1.5-flash" 

def ask_fast_ai(query):
    """
    Text-only query for the chat interface.
    """
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def ask_gemini_vision(image_input):
    """
    Robust Vision Analysis: Accepts Bytes, File Path, or PIL Image.
    """
    try:
        image = None
        if isinstance(image_input, str):
            if os.path.exists(image_input):
                image = Image.open(image_input)
            else:
                return "Object: Error\nStatus: Image file not found."
        elif isinstance(image_input, bytes):
            image = Image.open(io.BytesIO(image_input))
        else:
            image = Image.open(image_input)
        max_size = 1024
        if image.width > max_size or image.height > max_size:
            image.thumbnail((max_size, max_size))
        
        model = genai.GenerativeModel(MODEL_NAME)
        
        prompt = """
        Analyze this computer hardware component.
        1. Identify the specific part (Name, Model if visible).
        2. Check for visual physical damage (Burn marks, broken pins, rust, cracks).
        3. Classify status as: 'Healthy', 'Damaged', 'Critical', or 'Unknown'.
        
        Return the answer in this strict format:
        Object: [Name]
        Status: [Healthy/Damaged/Critical/Unknown] - [Brief Reason]
        """
        
        response = model.generate_content([prompt, image])
        return response.text
        
    except Exception as e:
        if "429" in str(e):
            return "Object: Error\nStatus: Cloud Vision Error (Rate Limit)"
        return f"Object: Error\nStatus: System Error - {str(e)}"