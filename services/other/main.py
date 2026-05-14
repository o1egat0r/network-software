"""Второй сервис за шлюзом: только маршрут /api/v1/other."""

from fastapi import FastAPI

app = FastAPI(title="other-mock")


@app.get("/api/v1/other")
def other_root() -> dict:
    return {"service": "other", "status": "ok"}
