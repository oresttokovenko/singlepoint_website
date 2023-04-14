# Use the Ubuntu 20.04 base image
FROM ubuntu:20.04

# Set working directory
WORKDIR /src

# Update package index and install required packages
RUN apt-get update && \
    apt-get install -y python3-pip nodejs zip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Create a virtual environment and install packages from requirements.txt
RUN python3 -m venv website-env && \
    . website-env/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port your web app will run on
EXPOSE 8080

# Activate the virtual environment and run your web app
CMD . website-env/bin/activate && \
    python3 src.py
