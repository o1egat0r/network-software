from fastapi import FastAPI, HTTPException
from starlette.responses import Response

from schemas import Comment, CommentCreate

app = FastAPI(title="comments-svc-s05 — ИА332, вариант 5")

_store: dict[int, Comment] = {}
_next_id: int = 1


@app.get("/comments")
def list_comments() -> list[dict]:
    return [c.model_dump() for c in _store.values()]


@app.post("/comments", status_code=201)
def create_comment(body: CommentCreate) -> dict:
    global _next_id
    c = Comment(id=_next_id, **body.model_dump())
    _store[_next_id] = c
    _next_id += 1
    return c.model_dump()


@app.get("/comments/{comment_id}")
def get_comment(comment_id: int) -> dict:
    if comment_id not in _store:
        raise HTTPException(status_code=404, detail="Комментарий не найден")
    return _store[comment_id].model_dump()


@app.put("/comments/{comment_id}")
def replace_comment(comment_id: int, body: CommentCreate) -> dict:
    if comment_id not in _store:
        raise HTTPException(status_code=404, detail="Комментарий не найден")
    c = Comment(id=comment_id, **body.model_dump())
    _store[comment_id] = c
    return c.model_dump()


@app.delete("/comments/{comment_id}", status_code=204)
def delete_comment(comment_id: int) -> Response:
    if comment_id not in _store:
        raise HTTPException(status_code=404, detail="Комментарий не найден")
    del _store[comment_id]
    return Response(status_code=204)
