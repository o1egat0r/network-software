from fastapi import FastAPI, HTTPException
from schemas import Booking, BookingCreate

app = FastAPI(title="bookings-svc-s05 — ИА332, вариант 5")

_store: dict[int, Booking] = {}
_next_id: int = 1


@app.get("/bookings")
def list_bookings() -> list[dict]:
    return [b.model_dump() for b in _store.values()]


@app.post("/bookings", status_code=201)
def create_booking(body: BookingCreate) -> dict:
    global _next_id
    booking = Booking(id=_next_id, **body.model_dump())
    _store[_next_id] = booking
    _next_id += 1
    return booking.model_dump()


@app.get("/bookings/{booking_id}")
def get_booking(booking_id: int) -> dict:
    if booking_id not in _store:
        raise HTTPException(status_code=404, detail="Бронирование не найдено")
    return _store[booking_id].model_dump()
