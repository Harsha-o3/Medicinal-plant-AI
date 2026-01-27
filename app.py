from flask import Flask, render_template, request, send_file
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from plant_info import plant_info
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"

# Load model
model = load_model("plant_classifier.h5")

class_labels = [
    "Ajwain","Alocasia plant","Aloe Plant","Amapalya","Angelica","Barberry",
    "Basil","Beechh Tree","Belladonna","Betel leaf","Black walnuts","Brahmi",
    "California","Coriander","Corn flower","Curry leaves","Fewer few","Garlic",
    "Gingko","Golden panthos","Hibiscus leaves","Horse Chestnuts","Horse tail",
    "Indian beech","Jack Fruit Leaves","Jade tail","Lavender","Liquirice root",
    "Malunggay","Mint","Mother wort","Neem","Papaya","Periwinkle",
    "Ponytail palm palm","Queen annes lace","Rauwolfia","Rosemary","Rubber plant",
    "Senna","Slippery Elm","Snake plant","Swiss plant","Tea leaves",
    "Terminalia leavees","Thyme","Turmeric leaves","Veronica","Winter Green",
    "yellow dock"
]

# -------------------------
# Utilities
# -------------------------
def preprocess(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0) / 255.0
    return img

def generate_pdf(plant, info):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, 750, f"Medicinal Plant Report: {plant}")

    y = 700
    c.setFont("Helvetica", 12)
    for k, v in info.items():
        c.drawString(50, y, f"{k.replace('_',' ').title()}: {v}")
        y -= 25

    c.save()
    buffer.seek(0)
    return buffer

# -------------------------
# Routes
# -------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)

        img = preprocess(path)
        preds = model.predict(img)
        idx = np.argmax(preds)
        plant = class_labels[idx]
        confidence = float(preds[0][idx] * 100)

        info = plant_info.get(plant)

        return render_template(
            "result.html",
            image=file.filename,
            plant=plant,
            confidence=confidence,
            info=info,
            preds=preds[0],
            labels=class_labels
        )

    return render_template("index.html")

@app.route("/download/<plant>")
def download_pdf(plant):
    info = plant_info.get(plant)
    pdf = generate_pdf(plant, info)
    return send_file(
        pdf,
        as_attachment=True,
        download_name=f"{plant}_report.pdf"
    )

if __name__ == "__main__":
    os.makedirs("static/uploads", exist_ok=True)
    app.run(debug=True)