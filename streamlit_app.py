import streamlit as st

def calculate_bmi(weight, height):
  """Calculates BMI based on weight and height."""
  bmi = weight / (height * height)
  return bmi

def interpret_bmi(bmi):
  """Interprets BMI value based on WHO classification."""
  if bmi < 18.5:
    return "Underweight"
  elif bmi < 25:
    return "Healthy weight"
  elif bmi < 30:
    return "Overweight"
  else:
    return "Obese"

st.title("BMI Calculator")

# Input fields for weight and height
weight = st.number_input("Enter your weight (kg):")
height = st.number_input("Enter your height (m):")

# Calculate BMI button
if st.button("Calculate BMI"):
  if weight > 0 and height > 0:
    bmi = calculate_bmi(weight, height)
    bmi_interpretation = interpret_bmi(bmi)
    
    # Display BMI and interpretation
    st.write("Your BMI is:", round(bmi, 2))
    st.write("BMI interpretation:", bmi_interpretation)
  else:
    st.warning("Please enter valid weight and height (positive values).")

