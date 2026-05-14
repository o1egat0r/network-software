"""Схемы для комментариев (лаб. 2, вариант 5, ИА332 — ресурс `comments`, поле `author`)."""

from pydantic import BaseModel


class CommentCreate(BaseModel):
    name: str
    author: str


class Comment(CommentCreate):
    id: int

    class Config:
        from_attributes = True
