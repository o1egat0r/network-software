# Multi-stage образ для tickets-s05 (порт 8204).
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
EXPOSE 8204
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8204"]
