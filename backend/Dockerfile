FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app ./app

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Render dynamically sets the PORT
ENV PORT=8000

EXPOSE ${PORT}

# Use shell form to allow variable expansion with production settings
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT} --workers 4 --proxy-headers