# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy alleen de map waar firewall.py in staat
COPY src/ /app

# Upgrade pip
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Expose poort
EXPOSE 80

# Start command
CMD ["python", "firewall.py"]
