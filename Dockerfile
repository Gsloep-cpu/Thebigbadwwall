# Gebruik Python 3.11 slim als basis
FROM python:3.11-slim

# Werkdirectory instellen
WORKDIR /app

# Kopieer de source code
COPY src/ .

# Kopieer requirements
COPY requirements.txt .

# Upgrade pip en installeer dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Zet de poort die Flask gaat gebruiken
EXPOSE 80

# Start de app (pas hier je bestandsnaam aan indien nodig)
CMD ["python", "main.py"]
