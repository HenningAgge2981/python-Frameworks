import tkinter as tk
from tkinter import messagebox


def arbeitszeit_berechnen():
    try:
        start = start_eingabe.get().split(":")
        ende = ende_eingabe.get().split(":")
        pause = int(pause_eingabe.get())

        start_minuten = int(start[0]) * 60 + int(start[1])
        ende_minuten = int(ende[0]) * 60 + int(ende[1])

        arbeitsminuten = ende_minuten - start_minuten - pause

        if arbeitsminuten < 0:
            raise ValueError

        stunden = arbeitsminuten // 60
        minuten = arbeitsminuten % 60

        ergebnis.config(text=f"Arbeitszeit: {stunden} Std. {minuten} Min.")
    except (ValueError, IndexError):
        messagebox.showerror("Ungültige Eingabe", "Bitte Zeiten als HH:MM eingeben.")


fenster = tk.Tk()
fenster.title("Arbeitszeitrechner")
fenster.geometry("350x250")
fenster.config(padx=25, pady=20)

tk.Label(fenster, text="Beginn, zum Beispiel 08:00").pack()
start_eingabe = tk.Entry(fenster)
start_eingabe.pack()

tk.Label(fenster, text="Ende, zum Beispiel 16:30").pack()
ende_eingabe = tk.Entry(fenster)
ende_eingabe.pack()

tk.Label(fenster, text="Pause in Minuten").pack()
pause_eingabe = tk.Entry(fenster)
pause_eingabe.insert(0, "30")
pause_eingabe.pack()

tk.Button(fenster, text="Berechnen", command=arbeitszeit_berechnen).pack(pady=15)

ergebnis = tk.Label(fenster, text="", font=("Arial", 12, "bold"))
ergebnis.pack()

fenster.mainloop()
