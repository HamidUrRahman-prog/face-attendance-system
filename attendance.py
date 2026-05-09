
import os
import numpy as np
from PIL import Image, ImageDraw
from deepface import DeepFace

FACES_DIR = "data/known_faces"

def load_known_faces(faces_dir=FACES_DIR):
    known_faces = []
    for filename in os.listdir(faces_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            name = os.path.splitext(filename)[0].replace("_", " ").title()
            path = os.path.join(faces_dir, filename)
            known_faces.append({"name": name, "path": path})
    return known_faces

def recognize_faces_in_image(image_array, known_faces):
    results = []
    temp_path = "temp_input.jpg"
    Image.fromarray(image_array).save(temp_path)
    try:
        detected = DeepFace.extract_faces(
            img_path=temp_path,
            detector_backend="opencv",
            enforce_detection=False
        )
    except:
        return results
    for face_data in detected:
        r = face_data["facial_area"]
        top = r["y"]
        left = r["x"]
        bottom = r["y"] + r["h"]
        right = r["x"] + r["w"]
        name, recognized = "Unknown", False
        for known in known_faces:
            try:
                res = DeepFace.verify(
                    img1_path=temp_path,
                    img2_path=known["path"],
                    model_name="VGG-Face",
                    detector_backend="opencv",
                    enforce_detection=False
                )
                if res["verified"]:
                    name, recognized = known["name"], True
                    break
            except:
                continue
        results.append({
            "name": name,
            "location": (top, right, bottom, left),
            "recognized": recognized
        })
    if os.path.exists(temp_path):
        os.remove(temp_path)
    return results

def draw_boxes(image_array, face_results):
    image = Image.fromarray(image_array)
    draw = ImageDraw.Draw(image)
    for face in face_results:
        top, right, bottom, left = face["location"]
        color = "#1D9E75" if face["recognized"] else "#E24B4A"
        draw.rectangle([left, top, right, bottom], outline=color, width=3)
        draw.rectangle([left, bottom, right, bottom + 24], fill=color)
        draw.text((left + 6, bottom + 4), face["name"], fill="white")
    return np.array(image)
