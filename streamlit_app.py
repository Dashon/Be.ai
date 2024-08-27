import streamlit as st
import requests
from datetime import datetime

def main():
    st.set_page_config(layout="wide")

    st.title("BE.AI")

    col1, col2, col3 = st.columns([0.35, 0.3, 0.35])

    with col1:
        st.subheader("Input")
        source_lang = st.selectbox(
            "Select source language",
            [
                "English",
                "African American Vernacular English",
                "Spanish",
            ],
        )
        with st.expander("Enter text to translate", expanded=True):
            text = st.text_area("", height=400, key="input_text_area")

    with col2:
        st.subheader("Settings")
        regional_variation = st.selectbox(
            "Select Regional Variation",
            [
                "Southern",
                "Northern",
                "West Coast",
                "Midwestern",
                "East Coast",
            ],
        )
        if regional_variation == "Custom Region":
            custom_region_traits = st.text_input(
                "Enter specific regional traits or preferences"
            )
        generational_influence = st.slider(
            "Generational Influence",
            min_value=0,
            max_value=100,
            value=50,
            help="Adjust to reflect the influence of older or younger generations on language.",
        )
        socio_economic_context = st.selectbox(
            "Socio-Economic Context",
            [
                "Urban Working-Class",
                "Middle-Class",
                "Professional/Academic",
            ],
            help="Select the socio-economic context to shape the language variation.",
        )
        cultural_influences = st.multiselect(
            "Cultural and Subcultural Influences",
            [
                "Hip-Hop/Rap Influence",
                "Social Media Influence",
                "Traditional/Conservative Influence",
            ],
            help="Select cultural influences to mix.",
        )
        code_switching = st.checkbox(
            "Enable Code-Switching",
            help="Allow language to switch between AAVE and Standard American English depending on context.",
        )
        if code_switching:
            code_switching_contexts = st.multiselect(
                "Customize Code-Switching Contexts",
                [
                    "Formal Settings",
                    "Casual Conversation",
                ],
            )
        geographical_setting = st.radio(
            "Geographical Setting",
            ["Rural", "Urban"],
            help="Choose whether the language reflects a rural or urban setting.",
        )

    translated_text = ""  # Initialize translated_text

    with col3:
        st.subheader("Output")
        target_lang = st.selectbox(
            "Select target language",
            [
                "African American Vernacular English",
                "English",
                "Spanish",
            ],
        )

    with col2:
        translate_button = st.button(
            "Translate", use_container_width=True, key="translate_button"
        )
        st.markdown(
            """
            <style>
            div.stButton > button:first-child {
                background-color: #4CAF50;
                color: white;
                width: 100%;
                height: 50px;
                font-size: 16px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

    if translate_button:
        request_payload = {
            "source_lang": source_lang,
            "target_lang": target_lang,
            "text": text,
            "regional_variation": regional_variation,
            "generational_influence": generational_influence,
            "socio_economic_context": socio_economic_context,
            "cultural_influences": cultural_influences,
            "code_switching": code_switching,
            "geographical_setting": geographical_setting,
        }

        response = requests.post("http://localhost:8000/translate/", json=request_payload)
        if response.status_code == 200:
            translated_text = response.json().get("translated_text", "Translation failed.")
        else:
            translated_text = "Error: " + response.text

        # Update the output panel with the translated text
        with col3:
            with st.expander("Translated Text", expanded=True):
                st.markdown(
                    f"<div style='height: 400px; overflow-y: auto;'>{translated_text}</div>",
                    unsafe_allow_html=True,
                )
