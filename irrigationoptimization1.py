inputs = None  # Initialize inputs outside the block

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
if inputs is not None:
    st.write(f"Inputs shape: {inputs.shape}")  # Debugging
else:
    st.write("Inputs are None")  # Debugging
