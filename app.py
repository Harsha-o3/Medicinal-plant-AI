from flask import Flask, render_template, request, send_file, redirect, url_for
import sqlite3
from datetime import datetime
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from plant_info import BOTANICAL_DATA, get_info, list_plants
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
# Database Initialization
# -------------------------
def init_db():
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  plant_name TEXT,
                  scientific_name TEXT,
                  confidence REAL,
                  image_path TEXT,
                  timestamp DATETIME)''')
    conn.commit()
    conn.close()

init_db()

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

        info = BOTANICAL_DATA.get(plant)
        sci_name = info.get('scientific_name', 'N/A') if info else 'N/A'

        # Save to History
        conn = sqlite3.connect('history.db')
        c = conn.cursor()
        c.execute("INSERT INTO history (plant_name, scientific_name, confidence, image_path, timestamp) VALUES (?, ?, ?, ?, ?)",
                  (plant, sci_name, confidence, file.filename, datetime.now()))
        conn.commit()
        conn.close()

        return render_template(
            "result.html",
            image=file.filename,
            plant=plant,
            confidence=confidence,
            info=info,
            preds=preds[0],
            labels=class_labels
        )

    # For GET request, fetch dashboard stats
    conn = sqlite3.connect('history.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # Get total scans
    c.execute("SELECT COUNT(*) FROM history")
    total_scans_row = c.fetchone()
    total_scans = total_scans_row[0] if total_scans_row else 0
    
    # Get recent 3 scans for home page preview
    c.execute("SELECT * FROM history ORDER BY timestamp DESC LIMIT 3")
    recent_history = [dict(ix) for ix in c.fetchall()]
    conn.close()
    
    # Get total plant species in our database
    total_species = len(list_plants())
    
    return render_template("index.html", 
                           total_scans=total_scans, 
                           recent_history=recent_history, 
                           total_species=total_species)

@app.route("/dashboard")
def dashboard():
    # Fetch dashboard stats
    conn = sqlite3.connect('history.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    # Get total scans
    c.execute("SELECT COUNT(*) FROM history")
    total_scans_row = c.fetchone()
    total_scans = total_scans_row[0] if total_scans_row else 0
    
    # Get recent 5 scans for dashboard
    c.execute("SELECT * FROM history ORDER BY timestamp DESC LIMIT 5")
    recent_history = [dict(ix) for ix in c.fetchall()]
    conn.close()
    
    # Get total plant species in our database
    total_species = len(list_plants())
    
    return render_template("dashboard.html", 
                           total_scans=total_scans, 
                           recent_history=recent_history, 
                           total_species=total_species)

@app.route("/download/<plant>")
def download_pdf(plant):
    info = BOTANICAL_DATA.get(plant)
    if not info:
        return redirect(url_for('index'))
    pdf = generate_pdf(plant, info)
    return send_file(
        pdf,
        as_attachment=True,
        download_name=f"{plant}_report.pdf"
    )

@app.route("/history")
def history():
    conn = sqlite3.connect('history.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM history ORDER BY timestamp DESC")
    history_data = c.fetchall()
    conn.close()
    return render_template("history.html", history=history_data)

if __name__ == "__main__":
    os.makedirs("static/uploads", exist_ok=True)
    app.run(debug=True)