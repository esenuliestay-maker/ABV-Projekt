import sqlite3
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models import Buchung

DB_PATH = "buchungen.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS buchungen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datum TEXT NOT NULL,
            betrag REAL NOT NULL,
            kategorie TEXT NOT NULL,
            typ TEXT NOT NULL,
            beschreibung TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


init_db()

app = FastAPI()

# Erlaubt dem Streamlit-Frontend (Port 8501), das Backend (Port 8000) anzusprechen
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.get("/")
def read_root():
    return {"status": "Das Backend läuft prima!"}


@app.post("/buchungen")
def buchung_erstellen(neue_buchung: Buchung):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO buchungen (datum, betrag, kategorie, typ, beschreibung) VALUES (?, ?, ?, ?, ?)",
        (str(neue_buchung.datum), neue_buchung.betrag, neue_buchung.kategorie, neue_buchung.typ, neue_buchung.beschreibung)
    )
    conn.commit()
    conn.close()
    return {"message": "Buchung gespeichert!"}


@app.get("/buchungen")
def buchungen_abrufen():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM buchungen", conn)
    conn.close()
    return df.to_dict(orient="records")


@app.delete("/buchungen/{buchung_id}")
def buchung_loeschen(buchung_id: int):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM buchungen WHERE id = ?", (buchung_id,))
    conn.commit()
    conn.close()
    return {"message": "Buchung gelöscht"}


@app.get("/auswertung/guv")
def guv_abrufen():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM buchungen", conn)
    conn.close()

    if df.empty:
        return {"einnahmen": 0.0, "ausgaben": 0.0, "ergebnis": 0.0}

    einnahmen = df[df["typ"] == "Einnahme"]["betrag"].sum()
    ausgaben = df[df["typ"] == "Ausgabe"]["betrag"].sum()

    return {
        "einnahmen": round(float(einnahmen), 2),
        "ausgaben": round(float(ausgaben), 2),
        "ergebnis": round(float(einnahmen - ausgaben), 2),
    }
