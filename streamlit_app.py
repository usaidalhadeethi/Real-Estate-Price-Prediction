import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("eniyi.joblib")

# Set up Streamlit app
st.title("Real Estate Price Prediction")

# Input fields for user
size = st.number_input("Size (in square meters):", min_value=50, max_value=300, step=1)
bedrooms = st.number_input("Number of Bedrooms:", min_value=1, max_value=5, step=1)
age = st.number_input("Age of the Property (in years):", min_value=0, max_value=50, step=1)
garden = st.selectbox("Does it have a garden?", ["No", "Yes"])
garage = st.selectbox("Does it have a garage?", ["No", "Yes"])
location = st.selectbox("Location:", ["Istanbul", "Ankara", "Izmir", "Bursa", "Antalya"])

# Convert user input to model format
location_modifiers = {"Istanbul": 0, "Ankara": 1, "Izmir": 2, "Bursa": 3, "Antalya": 4}
input_data = np.array([
    size,
    bedrooms,
    age,
    1 if garden == "Yes" else 0,
    1 if garage == "Yes" else 0,
    *(1 if i == location_modifiers[location] else 0 for i in range(1, 5))  # One-hot encoding for location
]).reshape(1, -1)

# Predict price
if st.button("Predict Price"):
    price = model.predict(input_data)
    st.success(f"The predicted price is: ${price[0]:,.2f}")
