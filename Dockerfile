# Use a lightweight Python 3.13 image
FROM python:3.13-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies for building some Python wheels
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy dependency file first for caching
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Cloud Run assigns PORT env var automatically
ENV PORT=8080
EXPOSE 8080

# Run Flask using Gunicorn
CMD exec gunicorn --bind :$PORT --workers 2 --threads 4 app:app
