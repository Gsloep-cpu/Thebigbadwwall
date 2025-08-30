# Gebruik een lichte Python 3.11 image
FROM python:3.11-slim

# Stel werkdirectory in
WORKDIR /app

# Kopieer de src map naar /app
COPY src/ /app

# Kopieer requirements
COPY requirements.txt /app/

# Upgrade pip
RUN python -m pip install --upgrade pip

# Installeer dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start het firewall script
CMD ["python", "firewall.py"]
