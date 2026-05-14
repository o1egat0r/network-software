# Отчёт по Docker (tickets-s05)

## Размер образа

После `docker build -t tickets-s05 .` в каталоге `weeks/week-10`:

- **Image size:** ~180 MB (python:3.11-slim + зависимости uvicorn/fastapi).

## Слои

- **Docker layer:** слой **FROM builder**: установка зависимостей в `/install` — отдельный слой кэша pip.
- Слой **COPY --from=builder**: копирование установленных пакетов в финальный образ.
- Слой **COPY . .**: код приложения — меняется чаще всего, поэтому идёт последним, чтобы не инвалидировать кэш pip.

## Сборка и запуск

```bash
docker build -t tickets-s05 .
docker run --rm -p 8204:8204 tickets-s05
```

Проект: **tickets-s05**.
