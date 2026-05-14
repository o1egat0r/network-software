"""Схемы для бронирований (вариант 5, группа ИА332).

Ранее здесь были модели товаров; для лабораторной 1 используется ресурс `bookings`
с полями `name` и `date` согласно `variants/332/s05/week-01.json`.
"""

from pydantic import BaseModel


class BookingCreate(BaseModel):
    name: str
    date: str


class Booking(BookingCreate):
    id: int

    class Config:
        from_attributes = True
