import streamlit as st
import pickle
import numpy as np

# Load your trained machine learning model (replace 'your_model.pkl' with your model's filename)
with open("your_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define the Streamlit app
st.title("Yield and Cost Optimization")
st.markdown("By Your Name")

st.subheader("Enter Yield and Cost:")
yield_input = st.number_input("Yield:")
cost_input = st.number_input("Cost:")

if st.button("Optimize"):
    # Ensure that the inputs are not empty
    if yield_input is not None and cost_input is not None:
        # Make predictions using your model
        inputs = np.array([[yield_input, cost_input]])
        prediction = model.predict(inputs)

        st.header("Optimization Result:")
        st.write(f"Predicted Yield: {prediction[0]:.2f}")

        # Optionally, you can provide additional information or analysis here
    else:
        st.subheader("Please enter both Yield and Cost values.")

# Optionally, you can provide an explanation or guidance to the user

# Debugging statements
st.write(f"Inputs shape: {inputs.shape}")  # Debugging
st.write(f"Model classes: {model.classes_}")  # Debugging
