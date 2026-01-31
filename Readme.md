# 🏖️ Tourism Product Prediction App

This repository contains a **Streamlit web application** that predicts whether a tourism product will be taken by a customer based on demographic and behavioral inputs.  
The app uses a **pretrained XGBoost model** hosted on [Hugging Face Hub](https://huggingface.co/ad3214/Tourism_model).

---

## 🚀 Features
- Interactive **Streamlit UI** for predictions
- Loads model directly from Hugging Face Hub (`ad3214/Tourism_model`)
- Inputs include:
  - Age
  - Duration of Pitch
  - Number of Trips
  - Monthly Income
  - Family Size
- Outputs:
  - ✅ Product Taken
  - ❌ Not Taken

---

## 📂 Repository Structure
Tourism_31/
├── app.py               # Streamlit app
├── requirements.txt     # Python dependencies
├── Dockerfile          # Container setup
└── README.md            # Documentation

---

## ⚙️ Installation & Usage

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/Tourism_31.git
cd Tourism_31

pip install -r requirements.txt
streamlit run app.py
docker build -t tourism-app .
docker run -p 8501:8501 tourism-app

