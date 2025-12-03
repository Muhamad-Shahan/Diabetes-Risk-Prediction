import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Page Layout
st.set_page_config(page_title="Diabetes Risk Predictor", page_icon="🩺", layout="centered")

# 1. Load the Saved Model
# We use @st.cache_resource so it loads fast
@st.cache_resource
def load_model():
    # Note: We are loading from the SAME folder, so no "models/" prefix needed
    with open('diabetes_model.pkl', 'rb') as f:
        data = pickle.load(f)
    return data

# Load data variables
data = load_model()
model = data["model"]
le_gender = data["le_gender"]
le_smoking = data["le_smoking"]

# 2. The Website Title
st.title("🩺 Diabetes Risk Predictor")
st.write("Enter your health metrics below to get a risk assessment.")

# 3. Input Form for User
st.subheader("Patient Details")
col1, col2 = st.columns(2)

with col1:
    # Dropdown for Gender
    gender = st.selectbox("Gender", le_gender.classes_)
    # Slider for Age
    age = st.slider("Age", 0, 120, 30)
    # Dropdowns for diseases
    hypertension = st.selectbox("Hypertension", ["No", "Yes"])
    heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])

with col2:
    # Dropdown for Smoking
    smoking = st.selectbox("Smoking History", le_smoking.classes_)
    # Number inputs for medical data
    bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
    hba1c = st.number_input("HbA1c Level", 3.0, 9.0, 5.5)
    glucose = st.number_input("Blood Glucose Level", 50, 300, 100)

# 4. Process Inputs for the Model
# Convert text inputs (Yes/No) into numbers (1/0)
gender_enc = le_gender.transform([gender])[0]
smoking_enc = le_smoking.transform([smoking])[0]
hyp_enc = 1 if hypertension == "Yes" else 0
heart_enc = 1 if heart_disease == "Yes" else 0

# Create the data row for the model
input_data = np.array([[gender_enc, age, hyp_enc, heart_enc, smoking_enc, bmi, hba1c, glucose]])

# 5. Predict Button
if st.button("Predict Risk"):
    prediction = model.predict(input_data)
    
    # Show Result
    if prediction[0] == 1:
        st.error("**Result: High Risk of Diabetes**")
        st.write("Please consult a healthcare professional.")
    else:
        st.success("**Result: Low Risk / Healthy**")
        st.write("Keep maintaining a healthy lifestyle!")