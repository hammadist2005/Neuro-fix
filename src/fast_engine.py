import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("API Key not found! Check your .env file.")

def ask_fast_ai(query):
    """
    Interfaces with Gemini 1.5 Flash for low-latency inference.
    """
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-flash-latest')

        system_context = (
            "You are Neuro-fix, a hardware diagnostic specialist. "
            "Diagnose PC issues (RAM, GPU, SSD, Motherboard) concisely and professionally. "
            "If pricing is mentioned, refer the user to the Market Data panel."
        )
        
        chat = model.start_chat(history=[
            {"role": "user", "parts": [system_context]},
            {"role": "model", "parts": ["Systems initialized. Ready for diagnostics."]}
        ])
        
        response = chat.send_message(query)
        return response.text

    except Exception as e:
        return f"Inference Error: {str(e)}"