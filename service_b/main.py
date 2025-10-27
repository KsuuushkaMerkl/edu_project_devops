from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
def get_info():
    return {"service": "B", "message": "Hello from Service B!", "status": "success"}
