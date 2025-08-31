FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    git \
    curl \
    libmagic-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install requirements
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    FILE_UPLOAD_DIR=/app/uploads

# Start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
