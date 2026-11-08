
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("water_model.pkl")

model = load_model()

# App title
st.title("Water Quality Prediction")

# Input fields
ph = st.number_input("pH", value=7.0)
hardness = st.number_input("Hardness", value=150.0)
solids = st.number_input("Solids", value=20000.0)
chloramines = st.number_input("Chloramines", value=7.0)
sulfate = st.number_input("Sulfate", value=300.0)
conductivity = st.number_input("Conductivity", value=400.0)
organic_carbon = st.number_input("Organic Carbon", value=10.0)
trihalomethanes = st.number_input("Trihalomethanes", value=60.0)
turbidity = st.number_input("Turbidity", value=4.0)

# Prediction button
if st.button("Predict Water Quality"):

    input_data = pd.DataFrame([{
        'ph': ph,
        'Hardness': hardness,
        'Solids': solids,
        'Chloramines': chloramines,
        'Sulfate': sulfate,
        'Conductivity': conductivity,
        'Organic_carbon': organic_carbon,
        'Trihalomethanes': trihalomethanes,
        'Turbidity': turbidity
    }])

    # Make prediction
    try:
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.success("Water is Potable. ✅")
        else:
            st.error("Water is Not Potable. ⚠️")

    except Exception as e:
        st.error(f"Prediction Error: {e}")
