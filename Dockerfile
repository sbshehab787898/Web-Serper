FROM python:3.9-slim

WORKDIR /app

# Install system dependencies if any needed for lxml or others
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Render provides port via PORT env var, but we default to 8000
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
