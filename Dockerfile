FROM python:3.11-slim-buster

# Set environment variables to minimize interactive prompts
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1

# Install necessary dependencies including LibreOffice
RUN apt-get update && apt-get install -y --no-install-recommends \
    libreoffice \
    libfontconfig1 \
    libfreetype6 \
    libx11-6 \
    libxrender1 \
    libxext6 \
    libxcb1 \
    libuuid1 \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY update_image.sh .
COPY requirements.txt .

# Install dependencies
RUN chmod +x update_image.sh && ./update_image.sh
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .
