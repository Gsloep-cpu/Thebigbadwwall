# Gebruik een lichte Python image
FROM python:3.11-slim

# Werkdirectory instellen
WORKDIR /app

# Kopieer requirements en installeer dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Kopieer de src map en Firewall.py naar de container
COPY src/ ./src
COPY Firewall.py .

# Stel het commando in om Firewall.py te draaien
CMD ["python", "Firewall.py"]
