# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port firewall zal gebruiken
EXPOSE 80

# Start command
CMD ["python", "firewall.py"]
