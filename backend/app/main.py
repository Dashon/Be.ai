from fastapi import FastAPI
from app.hello import hello
from app.routes import translation, vocabulary

app = FastAPI()

app.include_router(translation.router, prefix="/translate")
app.include_router(vocabulary.router, prefix="/vocab")

@app.get("/")
def read_root():
    return {"message": "Welcome to the AAVE Translation API"}
