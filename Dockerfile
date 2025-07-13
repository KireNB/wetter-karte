# Basis-Image mit Python
FROM python:3.11-slim

# Arbeitsverzeichnis
WORKDIR /app

# Abhängigkeiten installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App-Dateien kopieren
COPY . .

# Port freigeben
EXPOSE 5000

# Startbefehl
CMD ["python", "main.py"]


# FROM python:3.11-slim

# # Arbeitsverzeichnis setzen
# WORKDIR /app

# # Abhängigkeiten installieren
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Projektdateien kopieren
# COPY . .

# # PORT von Render verwenden
# ENV PORT=5000

# # Startbefehl
# CMD ["python", "main.py"]

####################################################################


# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD ["python", "main.py"]
