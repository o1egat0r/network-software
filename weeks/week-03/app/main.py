from fastapi import FastAPI
import os

app = FastAPI()
SERVICE_NAME = os.getenv("SERVICE_NAME", "events-service")

@app.get("/api/events")
async def get_events():
    return {"service": SERVICE_NAME, "data": "List of events"}

@app.get("/api/other")
async def get_other():
    return {"service": SERVICE_NAME, "data": "Other data"}

@app.get("/health")
async def health():
    return {"status": "ok"}