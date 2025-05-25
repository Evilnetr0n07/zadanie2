# syntax=docker/dockerfile:1
#etap budowania aplikacji
FROM python:3.11-slim AS builder

#dodanie informacji o autorze zgodnych z OCI
LABEL org.opencontainers.image.authors="Marek Zając"

#ustawienie katalogu roboczego
WORKDIR /app

#skopiowanie wymaganych zależności oraz ich instalacja
COPY requirements.txt .
RUN pip install --user -r requirements.txt

#etap uruchomienia aplikacji
FROM python:3.11-slim

#dodanie informacji o autorze zgodnych z OCI
LABEL org.opencontainers.image.authors="Marek Zając"

#ustawienie katalogu roboczego
WORKDIR /app

#skopiowanie danych z poprzedniego etapu
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

#skopiowanie potrzebnych plików aplikacji i szablonu
COPY . .

#stworzenie zmiennej środowiskowej definiującej port na którym ma działać aplikacja
ENV PORT=5000

#sprawdzenie czy aplikacja działa poprawnie
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s CMD curl --fail http://localhost:5000 || exit 1

#informacja na jakim porcie nasłuchuje informacja
EXPOSE 5000

#uruchomienie aplikacji
CMD ["python", "app.py"]

