import streamlit as st
import threading
from app.main import app, start

def main():
    # Start the FastAPI server in a separate thread
    server_thread = threading.Thread(target=start)
    server_thread.start()
    try:
        st.write("Welcome to the AAVE Translation App!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        if server_thread.is_alive():
            server_thread.join()

if __name__ == "__main__":
    main()
    # Uncomment the line below to run the FastAPI app
    # start()
