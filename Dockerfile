# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy src folder naar werkdirectory
COPY src/ /app

# Copy requirements en install dependencies
COPY requirements.txt /app/
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose poort voor firewall
EXPOSE 80

# Start de firewall
CMD ["python", "firewall.py"]
