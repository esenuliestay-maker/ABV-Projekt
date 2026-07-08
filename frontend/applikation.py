from datetime import date

import pandas as pd
import requests
import streamlit as st

BACKEND_URL = "http://localhost:8000"

st.title("Mein Buchungssystem")

st.header("Neue Buchung erfassen")

name = st.text_input("Beschreibung der Buchung")
datum = st.date_input("Datum")
typ = st.selectbox("Typ", options=["Einnahme", "Ausgabe"])
kategorie = st.text_input("Kategorie (z.B. Einkauf, Verkauf, Miete, Gehalt)")
ware = st.text_input("Ware / Produkt (z.B. Milka, Schogetten, Snickers, bei Buchungen, die Buchungen, die keine Ware betreffen, leer lassen.)")
betrag = st.number_input("Betrag (€)", min_value=0.0, step=1.0)

if st.button("Buchung abschicken"):
    # Wenn das Warenfeld leer ist, setzen wir "Allgemein" ein.
    if ware.strip() == "":
        ware = "Allgemein"

    daten = {
        "datum": str(datum),
        "beschreibung": name,
        "typ": typ,
        "kategorie": kategorie,
        "betrag": betrag,
        "ware": ware,
    }

    antwort = requests.post(f"{BACKEND_URL}/buchungen", json=daten)

    if antwort.status_code == 200:
        st.success(f"Buchung '{name}' über {betrag} € wurde gespeichert!")
    else:
        st.error("Fehler beim Speichern. Ist das Backend gestartet?")

st.header("Alle Buchungen")

try:
    antwort = requests.get(f"{BACKEND_URL}/buchungen")
    buchungen = antwort.json()

    if buchungen:
        df = pd.DataFrame(buchungen)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Noch keine Buchungen vorhanden.")
except requests.exceptions.ConnectionError:
    st.error("Backend nicht erreichbar. Bitte starte zuerst FastAPI.")

st.header("Gewinn- und Verlustrechnung (GuV)")

# Zeitraum fuer die GuV auswaehlen.
# Standard: vom 1. Januar des aktuellen Jahres bis heute.
guv_von = st.date_input("GuV von", value=date(date.today().year, 1, 1))
guv_bis = st.date_input("GuV bis", value=date.today())

try:
    params = {"von": str(guv_von), "bis": str(guv_bis)}
    guv = requests.get(f"{BACKEND_URL}/auswertung/guv", params=params).json()

    st.caption(f"Zeitraum: {guv_von} bis {guv_bis}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Einnahmen", f"{guv['einnahmen']} €")
    col2.metric("Ausgaben", f"{guv['ausgaben']} €")
    col3.metric("Ergebnis", f"{guv['ergebnis']} €")
except requests.exceptions.ConnectionError:
    st.error("GuV konnte nicht geladen werden.")

st.header("Warenvergleich und Investitionsentscheidung")

try:
    antwort = requests.get(f"{BACKEND_URL}/auswertung/waren")

    if antwort.status_code == 200:
        waren_auswertung = antwort.json()
        daten = waren_auswertung["daten"]

        if daten:
            waren_df = pd.DataFrame(daten)

            st.subheader("Vergleich nach Waren")
            st.dataframe(waren_df, use_container_width=True)

            st.subheader("Gewinn pro Ware")
            chart_df = waren_df.set_index("ware")[["einnahmen", "kosten", "gewinn"]]
            st.bar_chart(chart_df)

            st.subheader("Empfehlung")
            st.success(waren_auswertung["empfehlung"])
        else:
            st.info("Noch keine Waren-Daten vorhanden.")
    else:
        st.error("Warenvergleich konnte nicht geladen werden.")
except requests.exceptions.ConnectionError:
    st.error("Warenvergleich konnte nicht geladen werden. Bitte Backend starten.")

