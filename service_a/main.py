from fastapi import FastAPI
import requests
import time

app = FastAPI()

for i in range(10):
    try:
        requests.get("http://service_b:8001/info", timeout=2)
        break
    except Exception:
        print("Service B not ready, retrying...")
        time.sleep(3)

@app.get("/")
def root():
    return {"message": "Hello from Service A"}

@app.get("/from-b")
def get_from_b():
    try:
        response = requests.get("http://service_b:8001/info")
        data = response.json()
        return {"service": "A", "received": data}
    except Exception as e:
        return {"error": str(e)}
