import os
from dotenv import load_dotenv
import streamlit as st
import threading
import pyperclip
load_dotenv()

from main import app, start

# Load the OpenAI API key from the environment
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")


def main():
    # Start the FastAPI server in a separate thread
    server_thread = threading.Thread(target=start)
    server_thread.start()
    try:
        st.write("Welcome to the AAVE Translation App!")
        
        # Example translated text
        translated_text = "This is the translated text."

        # Display the translated text
        st.write(translated_text)

        # Add a button to copy the translated text to the clipboard
        if st.button("Copy to Clipboard"):
            pyperclip.copy(translated_text)
            st.success("Text copied to clipboard!")
    finally:
        if server_thread.is_alive():
            server_thread.join()


if __name__ == "__main__":
    main()
    # Uncomment the line below to run the FastAPI app
    # start()
