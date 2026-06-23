Semesterprojekt
|     |     |     |     | ABV | Programmieren | für WiWiss |
| --- | --- | --- | --- | --- | ------------- | ---------- |
Sommersemester 2026
Projektkontext
ImModulABV Programmieren für Wirtschaftswissenschaftler*innen habenwirunsimSemester
mit der Programmiersprache Python beschäftigt. Das Semesterprojekt dient dazu, die im Kurs
erarbeiteten Inhalte in einer kleinen, zusammenhängenden Anwendung praktisch anzuwenden.
Das Projekt ist unbenotet, soll aber zeigen, dass Sie eine überschaubare Softwareidee struktu-
| riert | umsetzen |     | können. |     |     |     |
| ----- | -------- | --- | ------- | --- | --- | --- |
Projektaufgabe
| Entwickeln |     | Sie | ein kleines | Buchungssystem |     | mit Python. |
| ---------- | --- | --- | ----------- | -------------- | --- | ----------- |
Ziel ist eine Anwendung, mit der Buchungen erfasst, gespeichert, abgerufen und in einer be-
triebswirtschaftlich sinnvollen Form ausgewertet werden können. Die Anwendung soll aus einem
| Frontend, |     | einem | Backend | und | einer Datenbank | bestehen. |
| --------- | --- | ----- | ------- | --- | --------------- | --------- |
Mindestanforderungen
Ihre Anwendung muss mindestens die folgenden Anforderungen erfüllen:
1. Frontend: Die Anwendung muss über ein Frontend nutzbar sein. Das Frontend soll mit
|     | Streamlit |     | umgesetzt | werden. |     |     |
| --- | --------- | --- | --------- | ------- | --- | --- |
2. Backend: Es muss ein Backend geben, das die Anwendungslogik kapselt und über eine
API angesprochen wird. Das Backend soll mit umgesetzt werden.
FastAPI
3. Die Anwendung muss Buchungen persistent speichern. Eine ein-
Datenbankanbindung:
fache relationale Datenbank, z.B. SQLite, ist dafür vollkommen ausreichend.
4. einfügen:NutzerinnenundNutzersollenüberdasFrontendneueBuchungen
Buchungen
|     | anlegen |     | können. |     |     |     |
| --- | ------- | --- | ------- | --- | --- | --- |
5. Bestehende Buchungen abrufen: Bereits gespeicherte Buchungen sollen im Frontend
|     | angezeigt |     | werden | können. |     |     |
| --- | --------- | --- | ------ | ------- | --- | --- |
6. Auswertung und Visualisierung: Die Anwendung soll auf Basis der erfassten Buchun-
gen mindestens betriebswirtschaftliche Auswertung visualisieren:
eine
|     |     | • entweder | eine | Bilanz | zu einem | Stichtag, |
| --- | --- | ---------- | ---- | ------ | -------- | --------- |
• oder eine GuV bis zu einem gewählten Datum bzw. für einen gewählten Zeitraum.
1

Die Auswertung soll im Frontend sichtbar sein und sich durch neu eingetragene Buchungen
aktualisieren.
7. Saubere Datenübergabe per API: Daten sollen strukturiert über die API zwischen
Frontend und Backend übergeben werden. Verwenden Sie dafür Pydantic zur Validierung
| und        | Typprüfung. |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- |
| Technische | Vorgaben    |     |     |     |     |
Für das Projekt gelten die folgenden technischen Rahmenbedingungen:
| •   |     | Streamlit |     |     |     |
| --- | --- | --------- | --- | --- | --- |
Frontend:
| •   | FastAPI |     |     |     |     |
| --- | ------- | --- | --- | --- | --- |
Backend:
| •   |     | Pydantic |     |     |     |
| --- | --- | -------- | --- | --- | --- |
Datenvalidierung:
| •   |     |     | Pandas |     |     |
| --- | --- | --- | ------ | --- | --- |
Datenverarbeitung:
| •   |     | Matplotlib | oder | eine vergleichbare | Bibliothek |
| --- | --- | ---------- | ---- | ------------------ | ---------- |
Visualisierung:
| Wichtig | ist die Trennung | der        | Komponenten: |                   |            |
| ------- | ---------------- | ---------- | ------------ | ----------------- | ---------- |
| • Das   | Frontend         | soll nicht | direkt       | auf die Datenbank | zugreifen. |
• Die Kommunikation soll über das Backend bzw. die API erfolgen.
• Das Backend übernimmt die Verarbeitung, Validierung und Speicherung der Daten.
Datenmodell
Ihr Datenmodell darf einfach gehalten sein, soll aber fachlich und technisch sinnvoll gewählt
werden. Als Orientierung kann der von mir bereitgestellte Beispieldatensatz samt Generator ver-
wendetwerden(sieheÜbung4-DatenAnalyseIfürgeneratorunddenDatensatz).DieNutzung
dieser Vorlage ist optional: Sie dürfen das Datenmodell ganz oder teilweise übernehmen, ver-
einfachen oder erweitern. Wenn Ihnen für Ihre Anwendung sinnvolle Felder fehlen, dürfen und
sollenSiedieseergänzen.EineBuchungsolltemindestensdiefolgendenInformationenenthalten:
| • ein   | Buchungsdatum,      |          |          |               |     |
| ------- | ------------------- | -------- | -------- | ------------- | --- |
| • einen | Betrag,             |          |          |               |     |
| • eine  | Kategorie           | oder ein | Konto,   |               |     |
| • einen | Buchungstyp,        | z.B.     | Einnahme | oder Ausgabe, |     |
| • eine  | kurze Beschreibung. |          |          |               |     |
Wichtig ist nicht, dass alle Felder des Beispieldatensatzes übernommen werden, sondern dass
Ihr Datenmodell zur Logik Ihrer Anwendung passt und die geforderten Funktionen sinnvoll
unterstützt.
| Kreative | Erweiterung |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- |
Zusätzlich zum Pflichtteil soll(en) Ihre Gruppe/(Sie) eine kreative Erweiterung entwickeln.
Diese Erweiterung soll Ihre Anwendung von anderen Projekten unterscheidbar machen. Wichtig:
Die kreative Erweiterung soll über eine sehr naheliegende Standardfunktion hinausge-
| hen. Mögliche | Richtungen | sind | zum Beispiel: |     |     |
| ------------- | ---------- | ---- | ------------- | --- | --- |
2

• Rollen im System mit bestimmten Fähigkeiten (Login mit Admin oder User)
| • ein Forecast      |     | für eine | Periode          | auf       | Basis vorhandener |              | Daten, |
| ------------------- | --- | -------- | ---------------- | --------- | ----------------- | ------------ | ------ |
| • eine ungewöhnlich |     |          | gute Interaktion |           | im Frontend,      |              |        |
| • ein Dashboard     |     | mit      | vertieften       | Analysen, |                   |              |        |
| • eine andere       |     | fachlich | oder             | technisch | interessante      | Erweiterung. |        |
Entscheidend ist, dass die Erweiterung eigenständig gedacht, sinnvoll integriert und im Re-
| pository sowie | in  | der Präsentation |     | klar | dargestellt | wird. |     |
| -------------- | --- | ---------------- | --- | ---- | ----------- | ----- | --- |
| Einsatz        | von | GenAI            |     |      |             |       |     |
Die Nutzung von GenAI ist erlaubt. Sie dürfen KI-Tools beispielsweise verwenden für:
• Ideenfindung
• Code-Snippets
• Debugging
• Dokumentation
| • Strukturierung |     | des | Projekts |     |     |     |     |
| ---------------- | --- | --- | -------- | --- | --- | --- | --- |
Voraussetzung ist jedoch vollständige Transparenz. Dokumentieren Sie im Repository klar:
| • welche | KI-Tools | Sie        | verwendet | haben,      |         |     |     |
| -------- | -------- | ---------- | --------- | ----------- | ------- | --- | --- |
| • wofür  | diese    | eingesetzt | wurden,   |             |         |     |     |
| • welche | Teile    | wesentlich | von       | KI erstellt | wurden, |     |     |
• welche Teile Sie selbst entwickelt oder eigenständig überarbeitet haben.
Diese Dokumentation kann entweder in der README.md oder in einer separaten Datei, z.B.
| AI_USAGE.md, | erfolgen. |     |     |     |     |     |     |
| ------------ | --------- | --- | --- | --- | --- | --- | --- |
Abgabe
Die Abgabe erfolgt über einen Link zu einem GitHub-Repository.
ausschließlich
| Abgabefrist: | 12.07.2026, |     | 23:59 | Uhr |     |     |     |
| ------------ | ----------- | --- | ----- | --- | --- | --- | --- |
Es wird der Repository-Link abgegeben. Maßgeblich ist der Stand des Repositories zum
nur
| Zeitpunkt der | Deadline. |     |     |     |     |     |     |
| ------------- | --------- | --- | --- | --- | --- | --- | --- |
Wichtig:
• WennIhrRepositoryprivatist,müssenSiedenGitHub-Nutzermickmolitorfreischalten.
• Ich kann nur Abgaben berücksichtigen, auf die ich tatsächlich Zugriff habe.
• Bewertetbzw.berücksichtigtwerdennurdieProjekte,dieichaufGitHubfindenundöffnen
kann.
3

Repository-Inhalt
Ihr GitHub-Repository soll mindestens die folgenden Dateien und Inhalte enthalten:
| • den  | vollständigen   |                 | Quellcode | der           | Anwendung, |        |            |     |
| ------ | --------------- | --------------- | --------- | ------------- | ---------- | ------ | ---------- | --- |
| • eine | pyproject.toml, |                 |           |               |            |        |            |     |
| • eine | uv.lock,        |                 |           |               |            |        |            |     |
| • eine | README.md.      |                 |           |               |            |        |            |     |
| Die    |                 | soll mindestens |           | die folgenden |            | Punkte | enthalten: |     |
README.md
| • die  | Namen        | der Gruppenmitglieder. |               |               |           |                |           |      |
| ------ | ------------ | ---------------------- | ------------- | ------------- | --------- | -------------- | --------- | ---- |
| • eine | kurze        | Beschreibung,          |               | was die       | Anwendung |                | macht,    |      |
| • eine | kurze        | Beschreibung,          |               | wie das       | Projekt   |                | aufgebaut | ist, |
| • eine | kurze        | Beschreibung           |               | der kreativen |           | Erweiterung,   |           |      |
| • eine | Anleitung    | zum                    | lokalen       | Starten       |           | der Anwendung, |           |      |
| • eine | transparente |                        | Dokumentation |               | der       | KI-Nutzung,    |           |      |
Die README darf bei Bedarf auch mit Unterstützung von KI erstellt werden, sofern dies kennt-
| lich gemacht | wird. |     |     |     |     |     |     |     |
| ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
Gruppengröße
Das Semesterprojekt kann allein oder in einer Gruppe von bearbeitet
maximal zwei Personen
werden. Tragt euch dafür bitte in folgende Tabelle ein: Anmeldeformular ABV
Präsentation
| Am 08.07.2026 |     | findet | die Präsentation |     | der | Anwendungen |     | statt. |
| ------------- | --- | ------ | ---------------- | --- | --- | ----------- | --- | ------ |
Bis zu diesem Termin soll Ihre Anwendung in einem funktionsfähigen Stand vorliegen. In der
| Präsentation   | sollen          | Sie | in 5     | bis 7 Minuten: |     |         |     |     |
| -------------- | --------------- | --- | -------- | -------------- | --- | ------- | --- | --- |
| • Ihre         | Anwendung       |     | kurz     | vorstellen,    |     |         |     |     |
| • die          | Grundfunktionen |     |          | demonstrieren, |     |         |     |     |
| • insbesondere |                 | die | kreative | Erweiterung    |     | zeigen. |     |     |
Bitte bringen Sie für die Präsentation Ihren eigenen Laptop mit HDMI-Anschluss mit.
Viel Erfolg
Ziel dieses Projekts ist nicht die perfekte Software, sondern eine verständliche, funktionieren-
de und sauber strukturierte Anwendung, in der die im Semester behandelten Inhalte sinnvoll
| zusammengeführt |     | werden. |     |     |     |     |     |     |
| --------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
Bei Rückfragen, Unklarheiten oder Anmerkungen, gerne jederzeit per Email (m.molitor@fu-
berlin.de) oder per Diskussionsforum im Blackboard an mich wenden.
4