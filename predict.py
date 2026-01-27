from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from plant_info import plant_info

# Load model
model = load_model("plant_classifier.h5")

# Class labels (same order used during training).
class_labels = [
    "Ajwain",
    "Alocasia plant",
    "Aloe Plant",
    "Amapalya",
    "Angelica",
    "Barberry",
    "Basil",
    "Beechh Tree",
    "Belladonna",
    "Betel leaf",
    "Black walnuts",
    "Brahmi",
    "California",
    "Coriander",
    "Corn flower",
    "Curry leaves",
    "Fewer few",
    "Garlic",
    "Gingko",
    "Golden panthos",
    "Hibiscus leaves",
    "Horse Chestnuts",
    "Horse tail",
    "Indian beech",
    "Jack Fruit Leaves",
    "Jade tail",
    "Lavender",
    "Liquirice root",
    "Malunggay",
    "Mint",
    "Mother wort",
    "Neem",
    "Papaya",
    "Periwinkle",
    "Ponytail palm palm",
    "Queen  annes  lace",
    "Rauwolfia",
    "Rosemary",
    "Rubber plant",
    "Senna",
    "Slippery Elm",
    "Snake plant",
    "Swiss plant",
    "Tea leaves",
    "Terminalia leavees",
    "Thyme",
    "Turmeric leaves",
    "Veronica",
    "Winter Green",
    "yellow dock",
]

def preprocess(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0) / 255.0
    return img

def predict(img_path):
    img = preprocess(img_path)
    preds = model.predict(img)
    idx = np.argmax(preds)
    plant_name = class_labels[idx]
    confidence = preds[0][idx]

    print(f"\nPredicted plant: {plant_name}")
    print(f"Confidence: {confidence*100:.2f}%")
    print("\nPharmacological Information:")
    print(plant_info.get(plant_name, "No info found"))

# Run prediction
predict(r"C:\Users\cheku\Desktop\medical pants\dataset\val\Ajwain\D2.jpg")  # Provide any plant image here
