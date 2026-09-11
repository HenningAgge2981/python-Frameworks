import pandas as pd

# Beispieldaten erzeugen
daten = pd.DataFrame(
    {
        "produkt": ["Laptop", "Maus", "Laptop", "Tastatur", "Maus"],
        "kategorie": ["Computer", "Zubehör", "Computer", "Zubehör", "Zubehör"],
        "preis": [899.00, 25.50, 949.00, 59.90, 29.50],
        "menge": [2, 10, 1, 5, 8],
    }
)

# Neue Spalte berechnen
daten["umsatz"] = daten["preis"] * daten["menge"]

print("Alle Verkaufsdaten:")
print(daten)

# Daten filtern
hohe_umsaetze = daten[daten["umsatz"] > 200]

print("Verkäufe mit mehr als 200 Euro Umsatz:")
print(hohe_umsaetze[["produkt", "umsatz"]])

# Nach Kategorie gruppieren
auswertung = daten.groupby("kategorie")["umsatz"].sum().sort_values(ascending=False)

print("Umsatz pro Kategorie:")
print(auswertung)

# Ergebnis als CSV speichern
auswertung.to_csv("auswertung.csv", header=["umsatz"])
print("Ergebnis wurde als auswertung.csv gespeichert.")
