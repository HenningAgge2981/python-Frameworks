import flet as ft


def main(page: ft.Page):
    page.title = "Meine Aufgaben"
    page.padding = 30

    eingabe = ft.TextField(label="Neue Aufgabe", expand=True)
    aufgaben = ft.Column()

    def hinzufuegen(event):
        text = eingabe.value.strip()

        if not text:
            eingabe.error_text = "Bitte eine Aufgabe eingeben."
            page.update()
            return

        eingabe.error_text = None
        aufgaben.controls.append(ft.Checkbox(label=text))
        eingabe.value = ""
        page.update()

    def erledigte_loeschen(event):
        aufgaben.controls = [aufgabe for aufgabe in aufgaben.controls if not aufgabe.value]
        page.update()

    page.add(
        ft.Text("Aufgabenliste", size=28, weight=ft.FontWeight.BOLD),
        ft.Row([eingabe, ft.ElevatedButton("Hinzufügen", on_click=hinzufuegen)]),
        aufgaben,
        ft.OutlinedButton("Erledigte löschen", on_click=erledigte_loeschen),
    )


ft.run(main)
