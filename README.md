# WSE Stock Tracker (GPW Data Pipeline)

Kompleksowy system do automatycznego pobierania, przechowywania i analizowania notowań spółek z Giełdy Papierów Wartościowych w Warszawie (GPW). 

Projekt prezentuje pełny przepływ danych (Data Pipeline) – od ich pozyskania (ETL), przez relacyjną bazę danych i własne REST API, aż po interaktywny frontend analityczny. Całość jest skonteneryzowana za pomocą Dockera, co ułatwia wdrożenie i uruchomienie w dowolnym środowisku.

## Główne funkcjonalności

* **Automatyczne pobieranie danych:** Skrypt łączy się z Yahoo Finance, aby pobierać najświeższe dane o polskich spółkach giełdowych.
* **REST API:** Aplikacja wystawia własne API, które pozwala na przeglądanie historii notowań oraz dynamiczne dodawanie nowych spółek do bazy.
* **Walidacja danych:** Bezpieczne przyjmowanie danych od użytkownika dzięki bibliotece Pydantic.
* **Interaktywny Dashboard:** Analityczny panel webowy pozwalający na filtrowanie spółek i przeglądanie ich historii cenowej na interaktywnych wykresach.
* **Konteneryzacja:** Pełna niezależność środowiskowa dzięki architekturze opartej na Docker Compose (osobny kontener na API, osobny na Frontend).

## Stack Technologiczny

**Backend / API:**
* [Python 3.11](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/) – Nowoczesny i szybki framework do budowy API.
* [SQLAlchemy](https://www.sqlalchemy.org/) – Mapowanie obiektowo-relacyjne (ORM).
* [yfinance](https://pypi.org/project/yfinance/) – Integracja z danymi giełdowymi.

**Baza Danych:**
* [SQLite](https://www.sqlite.org/) – Lekka, wbudowana relacyjna baza danych.

**Frontend / Analiza Danych:**
* [Streamlit](https://streamlit.io/) – Tworzenie interfejsu analitycznego.
* [Pandas](https://pandas.pydata.org/) – Manipulacja i obróbka danych.
* [Plotly](https://plotly.com/python/) – Generowanie interaktywnych wykresów.

**DevOps:**
* [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)

## Uruchomienie projektu (Lokalnie)

Aby uruchomić projekt na swoim komputerze, upewnij się, że masz zainstalowanego i włączonego **Docker Desktop**.

1. Sklonuj repozytorium:
   ```bash
   git clone [https://github.com/mateuszkowalczyk-git/wse-stock-tracker.git](https://github.com/mateuszkowalczyk-git/wse-stock-tracker.git)
   cd wse-stock-tracker
