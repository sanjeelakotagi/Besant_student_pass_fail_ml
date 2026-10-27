import pickle
import streamlit as st
# Set up the web page
st.title("�� Student Pass/Fail Predictor")
st.write("Enter the number of hours studied.")
# Load the saved ML model
with open("Besant_student_model.pkl", "rb") as file:
   model = pickle.load(file)
# Take input from the user
hours = st.number_input(
"Study hours",
min_value=0.0,
max_value=24.0,
value=4.0,
step=0.5
)
# Predict when the button is clicked
if st.button("Predict Result"):
# Get probabilities for both classes
   probability = model.predict_proba([[hours]])[0]

# Probability of Pass (class 1)
  pass_probability = probability[1]
# Decision threshold
  threshold = 0.5
# Apply threshold to decide Pass or Fail
if pass_probability>= threshold:
   st.success("Prediction: Pass")
   predicted_confidence = pass_probability
else:
   st.error("Prediction: Fail")
   predicted_confidence = probability[0]
# Display probabilities and threshold
st.write(f"Pass probability: {pass_probability * 100:.2f}%")
st.write(f"Fail probability: {probability[0] * 100:.2f}%")
st.write(f"Decision threshold: {threshold * 100:.0f}%")
st.write(
f"Probability of predicted class: "
f"{predicted_confidence * 100:.2f}%"
)
st.caption(
"Educational demonstration only. "
"This model is not suitable for real student assessment."
)
