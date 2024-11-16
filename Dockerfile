# Use an official Python runtime as a base image
FROM python:3.9-slim

# Install system dependencies required for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY app/requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application code into the container
COPY app/ /app/

# Copy the trained model file into the container
COPY model/LRCN_model.h5 /app/model/LRCN_model.h5

# Expose the port Flask is running on
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
