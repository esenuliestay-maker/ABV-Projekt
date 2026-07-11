Buchhaltungssystem Python Alkim und Yestay

Gruppenmitglieder

* [Yestay Yessenuly, 5603475]
* [Alkim Batu Kos, 5588811]

---

## Projektbeschreibung

Im Rahmen des Moduls **ABV Programmieren für Wirtschaftswissenschaftler*innen** haben wir ein Buchhaltungssystem entwickelt. Mit der Anwendung können Einnahmen und Ausgaben erfasst, dauerhaft gespeichert und anschließend ausgewertet werden.

Die Anwendung besteht aus einem Frontend, einem Backend und einer SQLite-Datenbank. Das Frontend dient zur Eingabe und Anzeige der Buchungen, während das Backend die Verarbeitung der Daten übernimmt. Die Kommunikation zwischen Frontend und Backend erfolgt über eine REST-API.

---

## Funktionen

Die Anwendung bietet folgende Funktionen:

* Erfassung neuer Buchungen
* Speicherung der Buchungen in einer SQLite-Datenbank
* Anzeige aller gespeicherten Buchungen
* Gewinn- und Verlustrechnung (GuV)
* Vergleich der Produkte
* Visualisierung der Ergebnisse mit einem Balkendiagramm
* Automatische Investitionsempfehlung auf Basis der berechneten Gewinne

---

## Projektaufbau

Das Projekt ist in Frontend und Backend aufgeteilt.

```text
ABV-Projekt
│
├── backend
│   ├── main.py
│   └── models.py
│
├── frontend
│   └── applikation.py
│
├── buchungen.db
├── pyproject.toml
├── uv.lock
└── README.md
```

### Frontend

Das Frontend wurde mit **Streamlit** umgesetzt. Hier können Buchungen eingegeben sowie alle Auswertungen angezeigt werden.

### Backend

Das Backend wurde mit **FastAPI** entwickelt. Es stellt die API bereit, verarbeitet die Anfragen aus dem Frontend und übernimmt die Kommunikation mit der Datenbank.

### Datenbank

Zur Speicherung der Buchungen wird eine SQLite-Datenbank verwendet.

---

## Kreative Erweiterung

Als kreative Erweiterung haben wir eine kleine betriebswirtschaftliche Entscheidungsunterstützung entwickelt.

Unser Beispiel basiert auf einem Verkaufsautomaten, der verschiedene Waren verkauft, z.B: **Milka** und **Schogetten**.

Für diese Produkte werden Umsatz, Kosten und Gewinn berechnet und miteinander verglichen. Anschließend gibt die Anwendung automatisch eine Empfehlung aus, welches Produkt im nächsten Geschäftsjahr stärker berücksichtigt werden sollte.

Ist der Gewinn der Produkte gleich hoch, empfiehlt das System, die bisherige Strategie beizubehalten.


---

## Verwendete Technologien

Für die Umsetzung wurden folgende Technologien verwendet:

* Python
* Streamlit
* FastAPI
* SQLite
* Pandas
* Pydantic
* Requests
* Matplotlib
* Git & GitHub
* uv

---

## Anwendung starten

### 1. Abhängigkeiten installieren

```bash
uv sync
```

### 2. Backend starten

```bash
uv run uvicorn backend.main:app --reload
```

### 3. Frontend starten

```bash
uv run streamlit run frontend/applikation.py
```

Nach dem Start kann die Anwendung im Browser verwendet werden.

---

## KI-Nutzung

Ehrlich gesagt, hatten wir am Anfang keine Ahnung, womit wir beginnen sollen und haben Chatgpt und Claude dafür gefragt, uns genaue Hinweise zu geben und Beispielcode zu erstellen, womit wir dann herausgehen konnten.

Für die weitere Entwicklung des Projekts wurden KI noch unterstützend eingesetzt.

Die KI wurde insbesondere verwendet für:

* Ideenfindung
* Unterstutzung bei einzelnen Codeabschnitten
* Fehlersuche (Debugging)
* Verbesserung der Projektstruktur
* Erstellung der Projektdokumentation
* Manchmal wurden ganze Zeilen von KI erstellt, da es uns schwer ging, die selbst zu       erfinden. Vor allem bei der Implementierung der originalen Idee.

Alle Vorschläge wurden von uns überprüft, angepasst und in das Projekt integriert. Die finale Anwendung wurde eigenständig getestet und weiterentwickelt.
