# Gebruik officiële Python-slim image
FROM python:3.11-slim

# Zet werkdirectory
WORKDIR /app

# Kopieer de src-map naar /app
COPY src/ /app

# Kopieer requirements
COPY requirements.txt /app/

# Upgrade pip
RUN python -m pip install --upgrade pip

# Installeer dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Toon de inhoud van /app voor debugging (optioneel, verwijder later)
# CMD ["ls", "-R", "/app"]

# Start je applicatie
# Pas hier het pad naar firewall.py aan als het in een submap staat
CMD ["python", "firewall.py"]
