# Use the official Python image as a base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required for building dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libhdf5-dev \
    pkg-config \
    git && \
    rm -rf /var/lib/apt/lists/*

# Copy and install dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your training script into the container
COPY test_train.py .
COPY test.py .
COPY test_.py .
COPY testDB.py .
# Command to keep the container running
# CMD ["tail", "-f", "/dev/null"]
CMD ["python", "test.py"]
