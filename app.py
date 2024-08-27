import os
from dotenv import load_dotenv
import streamlit as st
import threading
from dotenv import load_dotenv
import os
from main import app, start
from streamlit_app import main

load_dotenv()

# Load the OpenAI API key from the environment
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")


if __name__ == "__main__":
    # Start the FastAPI server in a separate thread
    server_thread = threading.Thread(target=start)
    server_thread.start()
    
    # Run the Streamlit app
    main()
    server_thread.join()
