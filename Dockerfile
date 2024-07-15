FROM python:3.12.4 AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY . .



RUN python -m venv .venv && \
    . .venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

FROM python:3.12.4-slim

WORKDIR /app
COPY --from=builder /app .

CMD ["/app/.venv/bin/fastapi", "run"]
