from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/from-b")
def get_from_b():
    try:
        response = requests.get("http://service_b:8001/info")
        data = response.json()
        return {"service": "A", "received": data}
    except Exception as e:
        return {"error": str(e)}
