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
            beschreibung TEXT NOT NULL,
            ware TEXT DEFAULT 'Allgemein'
        )
    """)

    # Falls eure alte Datenbank die Spalte "ware" noch nicht hat,
    # wird sie hier automatisch ergänzt.
    columns = conn.execute("PRAGMA table_info(buchungen)").fetchall()
    column_names = [column[1] for column in columns]

    if "ware" not in column_names:
        conn.execute("ALTER TABLE buchungen ADD COLUMN ware TEXT DEFAULT 'Allgemein'")

    conn.commit()
    conn.close()


def lade_buchungen_als_dataframe():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM buchungen", conn)
    conn.close()

    if not df.empty and "ware" not in df.columns:
        df["ware"] = "Allgemein"

    return df


init_db()

app = FastAPI(title="Buchungssystem API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"status": "Das Backend läuft."}


@app.post("/buchungen")
def buchung_erstellen(neue_buchung: Buchung):
    ware = neue_buchung.ware.strip() if neue_buchung.ware else "Allgemein"

    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        INSERT INTO buchungen
        (datum, betrag, kategorie, typ, beschreibung, ware)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            str(neue_buchung.datum),
            neue_buchung.betrag,
            neue_buchung.kategorie,
            neue_buchung.typ,
            neue_buchung.beschreibung,
            ware,
        ),
    )
    conn.commit()
    conn.close()

    return {"message": "Buchung gespeichert!"}


@app.get("/buchungen")
def buchungen_abrufen():
    df = lade_buchungen_als_dataframe()
    return df.to_dict(orient="records")


@app.delete("/buchungen/{buchung_id}")
def buchung_loeschen(buchung_id: int):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("DELETE FROM buchungen WHERE id = ?", (buchung_id,))
    conn.commit()
    conn.close()

    return {"message": "Buchung gelöscht."}


@app.get("/auswertung/guv")
def guv_abrufen():
    df = lade_buchungen_als_dataframe()

    if df.empty:
        return {
            "einnahmen": 0.0,
            "ausgaben": 0.0,
            "ergebnis": 0.0,
        }

    einnahmen = df[df["typ"] == "Einnahme"]["betrag"].sum()
    ausgaben = df[df["typ"] == "Ausgabe"]["betrag"].sum()
    ergebnis = einnahmen - ausgaben

    return {
        "einnahmen": round(float(einnahmen), 2),
        "ausgaben": round(float(ausgaben), 2),
        "ergebnis": round(float(ergebnis), 2),
    }


@app.get("/auswertung/waren")
def waren_auswertung():
    df = lade_buchungen_als_dataframe()

    if df.empty:
        return {
            "daten": [],
            "empfehlung": "Noch keine Buchungen vorhanden.",
        }

    df["ware"] = df["ware"].fillna("Allgemein")
    df["ware"] = df["ware"].replace("", "Allgemein")

    einnahmen = (
        df[df["typ"] == "Einnahme"]
        .groupby("ware")["betrag"]
        .sum()
        .reset_index(name="einnahmen")
    )

    kosten = (
        df[df["typ"] == "Ausgabe"]
        .groupby("ware")["betrag"]
        .sum()
        .reset_index(name="kosten")
    )

    auswertung = pd.merge(einnahmen, kosten, on="ware", how="outer").fillna(0)
    auswertung["gewinn"] = auswertung["einnahmen"] - auswertung["kosten"]

    auswertung["rendite_prozent"] = auswertung.apply(
        lambda row: round((row["gewinn"] / row["kosten"]) * 100, 2)
        if row["kosten"] > 0
        else 0,
        axis=1,
    )

    auswertung = auswertung.sort_values("gewinn", ascending=False)

    daten = auswertung.to_dict(orient="records")

    if len(auswertung) == 0:
        empfehlung = "Noch keine Waren-Daten vorhanden."
    elif len(auswertung) == 1:
        beste_ware = auswertung.iloc[0]["ware"]
        gewinn = round(float(auswertung.iloc[0]["gewinn"]), 2)

        if gewinn > 0:
            empfehlung = f"Investiere weiter in {beste_ware}, weil diese Ware aktuell Gewinn macht."
        elif gewinn < 0:
            empfehlung = f"Vorsicht bei {beste_ware}: Diese Ware macht aktuell Verlust."
        else:
            empfehlung = f"{beste_ware} ist aktuell genau bei 0 Euro Gewinn. Beobachte die Ware weiter."
    else:
        beste = auswertung.iloc[0]
        zweite = auswertung.iloc[1]

        bester_gewinn = float(beste["gewinn"])
        zweiter_gewinn = float(zweite["gewinn"])

        if bester_gewinn > zweiter_gewinn and bester_gewinn > 0:
            empfehlung = (
                f"Investiere mehr in {beste['ware']}, "
                f"weil diese Ware mit {round(bester_gewinn, 2)} Euro den höchsten Gewinn erzielt."
            )
        elif bester_gewinn <= 0:
            empfehlung = (
                "Keine Ware ist aktuell profitabel. "
                "Kaufe erstmal nicht mehr ein oder überprüfe Preise und Kosten."
            )
        else:
            empfehlung = (
                "Mach ungefähr genauso weiter wie letztes Jahr, "
                "weil keine Ware klar profitabler ist."
            )

    return {
        "daten": daten,
        "empfehlung": empfehlung,
    }