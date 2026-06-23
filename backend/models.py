from pydantic import BaseModel
from datetime import date


class Buchung(BaseModel):
    datum: date
    betrag: float
    kategorie: str
    typ: str  # "Einnahme" oder "Ausgabe"
    beschreibung: str
