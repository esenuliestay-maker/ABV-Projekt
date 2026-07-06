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


    conn.commit()
    conn.close()


def lade_buchungen_als_dataframe():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM buchungen", conn)
    conn.close()


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
    return {"status": "Das Backend lÃ¤uft."}


@app.post("/buchungen")
def buchung_erstellen(neue_buchung: Buchung):
    if neue_buchung.ware:
        ware = neue_buchung.ware.strip()
    else:
        ware = "Allgemein"

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

    return {"message": "Buchung gelÃ¶scht."}


@app.get("/auswertung/guv")
def guv_abrufen(von: str = None, bis: str = None):
    df = lade_buchungen_als_dataframe()

    if df.empty:
        return {
            "einnahmen": 0.0,
            "ausgaben": 0.0,
            "ergebnis": 0.0,
        }

    # Datum-Spalte in echte Datumswerte umwandeln, damit wir vergleichen können.
    df["datum"] = pd.to_datetime(df["datum"])

    # Nur Buchungen ab dem "Von"-Datum behalten (falls angegeben).
    if von is not None:
        df = df[df["datum"] >= pd.to_datetime(von)]

    # Nur Buchungen bis zum "Bis"-Datum behalten (falls angegeben).
    if bis is not None:
        df = df[df["datum"] <= pd.to_datetime(bis)]

    # Wenn im gewaehlten Zeitraum nichts liegt, geben wir 0 zurueck.
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

    # Allgemein sind keine echten Waren, sondern allgemeine Posten.
    # Deshalb werden sie im Warenvergleich nicht berücksichtigt.
    df = df[df["ware"] != "Allgemein"]

    if df.empty:
        return {
            "daten": [],
            "empfehlung": "Noch keine Waren-Daten vorhanden.",
        }

    ergebnisse = []

    for ware in df["ware"].unique():
        ware_df = df[df["ware"] == ware]

        einnahmen = ware_df[ware_df["typ"] == "Einnahme"]["betrag"].sum()
        kosten = ware_df[ware_df["typ"] == "Ausgabe"]["betrag"].sum()
        gewinn = einnahmen - kosten

        if kosten > 0:
            rendite_prozent = round((gewinn / kosten) * 100, 2)
        else:
            rendite_prozent = 0

        ergebnisse.append({
            "ware": ware,
            "einnahmen": round(float(einnahmen), 2),
            "kosten": round(float(kosten), 2),
            "gewinn": round(float(gewinn), 2),
            "rendite_prozent": rendite_prozent,
        })

    auswertung = pd.DataFrame(ergebnisse)
    auswertung = auswertung.sort_values("gewinn", ascending=False)
    daten = auswertung.to_dict(orient="records")

    if len(daten) == 0:
        empfehlung = "Noch keine Waren-Daten vorhanden."
    elif len(daten) == 1:
        beste_ware = daten[0]["ware"]
        gewinn = daten[0]["gewinn"]

        if gewinn > 0:
            empfehlung = f"Investiere weiter in {beste_ware}, weil diese Ware aktuell Gewinn macht."
        elif gewinn < 0:
            empfehlung = f"Vorsicht bei {beste_ware}: Diese Ware macht aktuell Verlust."
        else:
            empfehlung = f"{beste_ware} ist aktuell genau bei 0 Euro Gewinn. Beobachte die Ware weiter."
    else:
        beste = daten[0]
        zweite = daten[1]

        bester_gewinn = beste["gewinn"]
        zweiter_gewinn = zweite["gewinn"]

        if bester_gewinn > zweiter_gewinn and bester_gewinn > 0:
            empfehlung = (
                f"Investiere mehr in {beste['ware']}, "
                f"weil diese Ware mit {bester_gewinn} Euro den höchsten Gewinn erzielt."
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


