import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle


# Title
st.image("Logo.ipng")  # Assuming it's a IPNG file

st.title(" Insurance Premium Prediction")

# Input form
with st.form("insurance_form"):
    annual_income = st.number_input("Annual Income", min_value=1000, value=50000)
    credit_score = st.number_input("Credit Score", min_value=0, max_value=900, value=650)
    health_score = st.slider("Health Score", 0, 100, value=70)
    previous_claims = st.number_input("Previous Claims", min_value=0, value=0)
    age = st.number_input("Age", min_value=0, value=30)
    vehicle_age = st.number_input("Vehicle Age (years)", min_value=0, value= 10)
    insurance_duration = st.number_input("Insurance Duration (years)", min_value=0, value=10)
    num_dependents = st.number_input("Number of Dependents", min_value=0, value=1)
    education_level = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD", "Other"])
    exercise_frequency = st.selectbox("Exercise Frequency", ["Never", "Rarely", "Regularly", "Daily"])

    submitted = st.form_submit_button("Submit")

# Mapping for categorical values
education_order = {"High School": 0, "Bachelor's": 1, "Master's": 2, "PhD": 3}
exercise_order = {"Never": 0, "Rarely": 1, "Regularly": 2, "Daily": 3}


# On submit
if submitted:
    # Create DataFrame
    data = {
        "Annual Income":[annual_income],
        "Credit Score": [credit_score],
        "Health Score": [health_score],
        "Previous Claims": [previous_claims],
        "Age": [age],
        "Vehicle Age":[vehicle_age],
        "Insurance Duration": [insurance_duration],
        "Number of Dependents": [num_dependents],
        "Education Level": [education_order[education_level]],
        "Exercise Frequency": [exercise_order[exercise_frequency]],

    }

    df_input = pd.DataFrame(data)
 
    # 1. Load the pickled model
    with open('xgb_model.pkl','rb') as f:
        model = pickle.load(f)

    # 2. Load the pickled scaler
    with open('scaler.pkl','rb') as f:
        scaler = pickle.load(f)

    # 3. Load the test data (replace with actual file or DataFrame as needed)
    test_data = df_input  # You can replace this with pd.read_csv("your_test_file.csv")


    # 4. Apply the scaler to test data
    test_scaled = scaler.transform(test_data)

    # 5. Predict using the model
    predictions = model.predict(test_scaled)

    # 6. Inverse-transform predictions if model was trained on log1p(target)
    predictions_actual = np.expm1(predictions)

    # 7. Print predictions in original scale
    print(predictions_actual)


    # Display result
    st.success(f"✅ Predicted Insurance Premium Amount : ₹{int(predictions_actual):,.2f}")
    #st.write(int(predictions_actual))
