import streamlit as st
import requests

st.set_page_config(page_title="AAVE Translation App", layout="centered")

st.title("AAVE Translation App")
st.write("Translate text from English to African American Vernacular English (AAVE).")

text = st.text_area("Enter text to translate", "", height=150)

if st.button("Translate"):
    if text.strip():
        with st.spinner("Translating..."):
            try:
                response = requests.post("http://backend:8000/translate/", json={
                    "text": text,
                    "source_lang": "en",
                    "target_lang": "aave"
                })
                response.raise_for_status()
                translated_text = response.json().get("translated_text", "")
                st.success("Translation successful!")
                st.write("### Translated Text:")
                st.write(translated_text)
            except requests.exceptions.RequestException as e:
                st.error(f"Error in translation: {e}")
    else:
        st.warning("Please enter text to translate.")
