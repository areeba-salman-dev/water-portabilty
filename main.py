
import streamlit as st
import pandas as pd
import joblib

@st.cache_resource
def load_model():
    
    return joblib.load('water_model.pkl')

model = load_model()
st.title("Water Quality Prediction")

ph = st.number_input("pH", value=7.0)
Hardness = st.number_input("Hardness", value=150.0)
Solids = st.number_input("Solids", value=20000.0)
Chloramines = st.number_input("Chloramines", value=7.0)
Sulfate = st.number_input("Sulfate", value=300.0)
Conductivity = st.number_input("Conductivity", value=400.0)
Organic_carbon = st.number_input("Organic Carbon", value=10.0)
Trihalomethanes = st.number_input("Trihalomethanes", value=60.0)
Turbidity = st.number_input("Turbidity", value=4.0)

if st.button("Predict Water Quality"):

    input_data = pd.DataFrame([{
        'ph': ph,
        'Hardness': Hardness,
        'Solids': Solids,
        'Chloramines': Chloramines,
        'Sulfate': Sulfate,
        'Conductivity': Conductivity,
        'Organic_carbon': Organic_carbon,
        'Trihalomethanes': Trihalomethanes,
        'Turbidity': Turbidity
    }])

    st.write("Input Data:")
    st.dataframe(input_data)

    st.success("Input submitted successfully!")
if submitted:

    if not hasattr(model, "predict"):
        st.error(f"Invalid model object: {type(model)}")
        st.write("PKL contents:", repr(model))
    else:
        new_data = np.array([[
            ph, hardness, solids, chloramines, sulfate,
            conductivity, organic_carbon, trihalomethanes, turbidity
        ]])

        predictions = model.predict(new_data)

        if predictions[0] == 1:
            st.success("Water is Potable.", icon="✅")
        else:
            st.error("Water is Not Potable.", icon="⚠️")
