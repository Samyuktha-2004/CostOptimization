import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics import r2_score

# Load your trained machine learning model (replace 'your_model.pkl' with your model's filename)
with open("irrigationOptimization.pkl", "rb") as file:
    model = pickle.load(file)

# Define the Streamlit app
st.title("Yield and Cost Optimization")
st.markdown("Datathon2.0")

st.subheader("Enter Yield and Cost:")
yield_input = st.number_input("Yield:")
cost_input = st.number_input("Cost:")

if st.button("Optimize"):
    # Make predictions using your model
    prediction = model.predict([[yield_input, cost_input]])[0]

    st.header("Optimization Result:")
    st.write(f"Predicted Yield: {prediction:.2f}")

    # Calculate the R2 score (you'll need actual yield values for this)
    actual_yield =  0.8647847452107349
    # Provide actual yield value here
    r2 = r2_score([actual_yield], [prediction])
    st.write(f"R2 Score: {r2:.2f}")

# Optionally, you can provide an explanation or guidance to the user

