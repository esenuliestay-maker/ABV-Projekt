from datetime import date
from typing import Literal

from pydantic import BaseModel


class Buchung(BaseModel):
    datum: date
    betrag: float
    kategorie: str
    typ: Literal["Einnahme", "Ausgabe"]
    beschreibung: str
    ware: str = "Allgemein"