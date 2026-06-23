import streamlit as st
import pandas as pd
import requests

BACKEND_URL = "http://localhost:8000"

st.title("Mein Buchungssystem")

# ── 1. Buchung erfassen ──────────────────────────────────────────────────────
st.header("Neue Buchung erfassen")

name = st.text_input("Beschreibung der Buchung")
datum = st.date_input("Datum")
typ = st.selectbox("Typ", options=["Einnahme", "Ausgabe"])
kategorie = st.text_input("Kategorie (z.B. Miete, Gehalt, Verkauf)")
betrag = st.number_input("Betrag (€)", min_value=0.0)

if st.button("Buchung abschicken"):
    daten = {
        "datum": str(datum),
        "beschreibung": name,
        "typ": typ,
        "kategorie": kategorie,
        "betrag": betrag,
    }
    antwort = requests.post(f"{BACKEND_URL}/buchungen", json=daten)
    if antwort.status_code == 200:
        st.success(f"Buchung '{name}' über {betrag} € wurde gespeichert!")
    else:
        st.error("Fehler beim Speichern. Ist das Backend gestartet?")

# ── 2. Alle Buchungen anzeigen ───────────────────────────────────────────────
st.header("Alle Buchungen")

antwort = requests.get(f"{BACKEND_URL}/buchungen")
buchungen = antwort.json()

if buchungen:
    df = pd.DataFrame(buchungen)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Noch keine Buchungen vorhanden.")

# ── 3. GuV-Auswertung ────────────────────────────────────────────────────────
st.header("Gewinn- und Verlustrechnung (GuV)")

guv = requests.get(f"{BACKEND_URL}/auswertung/guv").json()

col1, col2, col3 = st.columns(3)
col1.metric("Einnahmen", f"{guv['einnahmen']} €")
col2.metric("Ausgaben",  f"{guv['ausgaben']} €")
col3.metric("Ergebnis",  f"{guv['ergebnis']} €")
