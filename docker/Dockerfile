# Użyj obrazu bazowego Pythona 3.9
FROM python:3.9-slim

# Ustaw katalog roboczy
WORKDIR /backend

# Skopiuj pliki aplikacji FastAPI do kontenera
COPY ./backend /backend

# Zainstaluj zależności Pythona
RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# Uruchom FastAPI na porcie 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
