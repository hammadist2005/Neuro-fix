from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np
import google.generativeai as genai
import re
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)
vision_model = genai.GenerativeModel('gemini-flash-latest')

local_model = YOLO('yolov8n.pt')

def analyze_image(image_path):
    """
    1. Uses YOLO to draw a Red Bounding Box (Visual Effect).
    2. Uses Gemini to IDENTIFY the object and CHECK for damage.
    """
    results = local_model(image_path)
    result = results[0]
    
    if len(result.boxes) > 0:
        annotated_bgr = result.plot(labels=False, conf=False)
        annotated_rgb = cv2.cvtColor(annotated_bgr, cv2.COLOR_BGR2RGB)
        Image.fromarray(annotated_rgb).save("annotated_temp.jpg")
    else:
        Image.open(image_path).save("annotated_temp.jpg")
        
    detected_object = "Hardware"
    damage_report = "Analysis Failed"
    
    try:
        img_file = Image.open(image_path)
        prompt = (
            "Analyze this image of computer hardware. "
            "1. Identify the specific component (e.g., RAM Stick, NVMe SSD, GPU, Motherboard). "
            "2. Analyze it strictly for PHYSICAL DAMAGE (burns, cracks, broken pins). "
            "Return the answer in this EXACT format: "
            "Object: [Component Name] | Condition: [Healthy/Critical/Damaged] - [Brief explanation]"
        )
        
        response = vision_model.generate_content([prompt, img_file])
        raw_text = response.text.strip()
        
        if "Object:" in raw_text and "|" in raw_text:
            parts = raw_text.split("|")
            detected_object = parts[0].replace("Object:", "").strip()
            damage_report = parts[1].replace("Condition:", "").strip()
        else:
            detected_object = "Hardware Component"
            damage_report = raw_text

    except Exception as e:
        damage_report = "Cloud Vision Error: Check Internet"

    return detected_object, damage_report