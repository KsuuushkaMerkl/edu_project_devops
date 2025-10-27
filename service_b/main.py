from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Service B"}

@app.get("/info")
def info():
    return {"service": "B", "status": "OK"}
