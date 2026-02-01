🌿 Medicinal Plant AI
A Flask-based web application powered by Machine Learning that classifies medicinal plants from images and provides detailed information about their uses, benefits, and applications in healthcare.
This project leverages deep learning (CNN) models for plant classification and integrates a user-friendly interface for real-time predictions.

🚀 Features
- Image Upload & Classification: Upload plant images to identify medicinal species.
- CNN Model Integration: Uses a trained deep learning model (plant_classifier.h5) for accurate predictions.
- Plant Information: Provides detailed medicinal uses, benefits, and applications via plant_info.py.
- Data Visualization: Includes confusion matrix and classification metrics for model evaluation.
- Web Interface: Flask-based frontend with templates for easy interaction.
- Deployment Ready: Configured for cloud deployment (Render/Netlify/Vercel).

🛠 Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- Machine Learning: TensorFlow, Keras, NumPy, Pandas, Scikit-learn
- Database: MySQL (optional for storing plant info)
- Tools: Git, VS Code, REST APIs
- Deployment: Render

📂 Project Structure
Medicinal-plant-AI/
│── app.py                # Main Flask application
│── classification.ipynb  # Jupyter Notebook for training & evaluation
│── plant_classifier.h5   # Trained CNN model
│── plant_info.py         # Plant details and medicinal uses
│── predict.py            # Prediction logic
│── requirements.txt      # Dependencies
│── templates/            # HTML templates
│── static/uploads/       # Uploaded images
│── confusion_matrix.png  # Model evaluation visualization
│── README.md             # Project documentation



⚙️ Installation & Usage
- Clone the repository
git clone https://github.com/Harsha-o3/Medicinal-plant-AI.git
cd Medicinal-plant-AI
- Install dependencies
pip install -r requirements.txt
- Run the Flask app
python app.py
- Open in browser
Navigate to http://127.0.0.1:5000 to use the web app.

📊 Model Details
- Architecture: Convolutional Neural Network (CNN)
- Dataset: Medicinal plant images (custom dataset)
- Evaluation: Confusion matrix and accuracy metrics included
- Output: Plant name + medicinal uses

🌱 Future Enhancements
- Expand dataset for more plant species.
- Integrate multilingual support for plant information.
- Add mobile-friendly UI.
- Deploy with Docker for portability.

🤝 Contributing
Contributions are welcome! Please fork the repo and submit a pull request with improvements.
