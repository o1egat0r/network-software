"""Сервис событий за шлюзом: префикс /api/events (неделя 3, вариант 5)."""

from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import Response

router = APIRouter(prefix="/api/events")


class EventCreate(BaseModel):
    name: str
    location: str


class Event(EventCreate):
    id: int


_store: dict[int, Event] = {}
_next_id: int = 1


@router.get("/")
def list_events() -> list[dict]:
    return [e.model_dump() for e in _store.values()]


@router.post("/", status_code=201)
def create_event(body: EventCreate) -> dict:
    global _next_id
    e = Event(id=_next_id, **body.model_dump())
    _store[_next_id] = e
    _next_id += 1
    return e.model_dump()


@router.get("/{event_id}")
def get_event(event_id: int) -> dict:
    if event_id not in _store:
        raise HTTPException(status_code=404, detail="Событие не найдено")
    return _store[event_id].model_dump()


@router.put("/{event_id}")
def replace_event(event_id: int, body: EventCreate) -> dict:
    if event_id not in _store:
        raise HTTPException(status_code=404, detail="Событие не найдено")
    e = Event(id=event_id, **body.model_dump())
    _store[event_id] = e
    return e.model_dump()


@router.delete("/{event_id}", status_code=204)
def delete_event(event_id: int) -> Response:
    if event_id not in _store:
        raise HTTPException(status_code=404, detail="Событие не найдено")
    del _store[event_id]
    return Response(status_code=204)


app = FastAPI(title="events-svc-s05")
app.include_router(router)
