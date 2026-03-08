import streamlit as st
import requests

st.title("AI Exam Anxiety Detector")

text = st.text_area("Enter how you feel about your exam")

if st.button("Analyze Anxiety"):

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"text": text}
    )

    result = response.json()["prediction"]

    if result == "Low":
        st.success("Low Anxiety 😊")

    elif result == "Moderate":
        st.warning("Moderate Anxiety 😐")

    else:
        st.error("High Anxiety 😟")