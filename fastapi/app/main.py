from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}


@app.get("/health")
def health():
    return {"status": "ok"}