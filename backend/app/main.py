import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.hello import hello
from app.routes import translation, vocabulary

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(translation.router, prefix="/translate")
app.include_router(vocabulary.router, prefix="/vocab")


@app.get("/")
def read_root():
    return hello()


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    start()
