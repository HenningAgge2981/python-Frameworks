import pandas as pd
import streamlit as st

st.set_page_config(page_title="Umsatz-Dashboard", page_icon="📊")
st.title("📊 Umsatz-Dashboard")

daten = pd.DataFrame(
    {
        "produkt": ["Laptop", "Maus", "Tastatur", "Monitor"],
        "kategorie": ["Computer", "Zubehör", "Zubehör", "Computer"],
        "preis": [899.00, 25.50, 59.90, 249.00],
        "menge": [2, 10, 5, 3],
    }
)

daten["umsatz"] = daten["preis"] * daten["menge"]

kategorie = st.selectbox("Kategorie auswählen", ["Alle"] + sorted(daten["kategorie"].unique()))

if kategorie != "Alle":
    anzeige = daten[daten["kategorie"] == kategorie]
else:
    anzeige = daten

st.metric("Gesamtumsatz", f"{anzeige['umsatz'].sum():,.2f} €")
st.dataframe(anzeige, use_container_width=True)

diagramm = anzeige.set_index("produkt")["umsatz"]
st.bar_chart(diagramm)

if st.button("Erfolgreich ausgewertet"):
    st.success("Die Auswertung ist abgeschlossen!")
