
import streamlit as st
import xgboost as xgb
import pandas as pd
from huggingface_hub import hf_hub_download

# Load model from Hugging Face Hub
model_path = hf_hub_download(repo_id="ad3214/Tourism_model", filename="best_model.json")
model = xgb.XGBClassifier()
model.load_model(model_path)

st.title("🏖️ Tourism Product Prediction App")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)
duration = st.number_input("Duration Of Pitch", min_value=1, max_value=60, value=10)
trips = st.number_input("Number Of Trips", min_value=0, max_value=50, value=2)
income = st.number_input("Monthly Income", min_value=1000, max_value=100000, value=20000)
family_size = st.number_input("Family Size", min_value=1, max_value=20, value=4)

if st.button("Predict"):
    df = pd.DataFrame([{
        "Age": age,
        "DurationOfPitch": duration,
        "NumberOfTrips": trips,
        "MonthlyIncome": income,
        "FamilySize": family_size
    }])
    preds = model.predict(df)
    result = "✅ Product Taken" if preds[0] == 1 else "❌ Not Taken"
    st.success(result)
