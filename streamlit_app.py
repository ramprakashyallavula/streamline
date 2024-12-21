import streamlit as st
import requests

# FastAPI endpoint URL
API_URL = "https://e-commerce-517y.onrender.com/predict/"

# Streamlit app title
st.title("Ecommerce Sales Prediction App")
st.header("Enter Data for Prediction")

# Input fields for user data
category = st.number_input("Category (as a float)", value=0.0)
revenue = st.number_input("Revenue (as a float)", value=0.0)
price = st.number_input("Price (as a float)", value=0.0)
quantity = st.number_input("Quantity (as a float)", value=0.0)

# Submit button
if st.button("Predict"):
    # Prepare the input data for the API
    data = {
        "Category": category,
        "Revenue": revenue,
        "Price": price,
        "Quantity": quantity
    }

    # Send a POST request to the FastAPI endpoint
    try:
        response = requests.post(API_URL, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        result = response.json()
        # Display the prediction result
        st.success(f"Predicted Sales: {result['prediction']}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")