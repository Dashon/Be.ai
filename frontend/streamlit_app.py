import streamlit as st
import requests

st.title("AAVE Translation App")

text = st.text_area("Enter text to translate", "")

if st.button("Translate"):
    response = requests.post("http://backend:8000/translate/", json={
        "text": text,
        "source_lang": "en",
        "target_lang": "aave"
    })
    if response.status_code == 200:
        translated_text = response.json().get("translated_text", "")
        st.write("Translated Text:")
        st.write(translated_text)
    else:
        st.write("Error in translation")
