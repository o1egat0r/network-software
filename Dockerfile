FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /home/worker/app
COPY . .

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && useradd -m worker \
    && pip3 install --no-cache-dir -r requirements.txt \
    && chown -R worker:worker /home/worker/app \
    && rm -rf /var/lib/apt/lists/*

USER worker

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]