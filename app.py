import streamlit as st
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

def hello():
    return {"message": "Hello from the AAVE Translation API"}

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return hello()

def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run(app, host="0.0.0.0", port=8000)

def main():
    st.title("AAVE Translation App")
    st.write("Welcome to the AAVE Translation App!")

if __name__ == "__main__":
    main()
    # Uncomment the line below to run the FastAPI app
    # start()
