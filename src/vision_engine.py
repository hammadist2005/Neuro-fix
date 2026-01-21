from ultralytics import YOLO
from PIL import Image, ImageDraw
import os

def analyze_image(image_path):
    # --- 1. Model Loading Logic (From your old code) ---
    # Try to find your custom trained model first
    model_path = os.path.join(os.path.dirname(__file__), '../models/best.pt')
    
    if not os.path.exists(model_path):
        # Fallback to default if custom model is missing
        print("Custom model not found. Using default YOLOv8n.")
        model_path = 'yolov8n.pt' 
    
    # Load the model
    model = YOLO(model_path)
    
    # --- 2. Safety Check ---
    if not os.path.exists(image_path):
        return "None"

    try:
        # Run inference
        results = model(image_path)
        result = results[0]
        
        detected_name = "None"
        
        # --- 3. Bounding Box Logic (The new "Pro" feature) ---
        if len(result.boxes) > 0:
            # Get the highest confidence detection
            box = result.boxes[0]
            class_id = int(box.cls[0])
            detected_name = model.names[class_id]
            
            # Get coordinates [x1, y1, x2, y2]
            cords = box.xyxy[0].tolist()
            cords = [int(x) for x in cords]
            
            # Draw the red box on the image file
            with Image.open(image_path) as img:
                draw = ImageDraw.Draw(img)
                draw.rectangle(cords, outline="red", width=5)
                img.save(image_path)
            
        return detected_name
        
    except Exception as e:
        print(f"Vision Error: {e}")
        return "None"