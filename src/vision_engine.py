from ultralytics import YOLO
import os

def analyze_image(image_path):
    # Check if custom model exists, otherwise use default
    model_path = 'models/best.pt'
    if not os.path.exists(model_path):
        print("Custom model not found. Using default YOLOv8n.")
        model_path = 'yolov8n.pt' 

    model = YOLO(model_path)
    results = model(image_path)
    
    # Return the name of the first object seen
    for result in results:
        if result.boxes:
            class_id = int(result.boxes.cls[0])
            return model.names[class_id]
    return None