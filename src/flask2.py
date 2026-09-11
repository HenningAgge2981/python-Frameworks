from flask import Flask, jsonify, request

app = Flask(__name__)

aufgaben = [
    {"id": 1, "titel": "Python lernen", "erledigt": False},
    {"id": 2, "titel": "Präsentation halten", "erledigt": True},
]


@app.get("/")
def startseite():
    return """
    <h1>Aufgaben-API</h1>
    <p>GET /api/aufgaben</p>
    <p>POST /api/aufgaben</p>
    """


@app.get("/api/aufgaben")
def alle_aufgaben():
    return jsonify(aufgaben)


@app.post("/api/aufgaben")
def aufgabe_anlegen():
    daten = request.get_json(silent=True) or {}
    titel = daten.get("titel", "").strip()

    if not titel:
        return jsonify({"fehler": "Titel fehlt"}), 400

    neue_aufgabe = {"id": len(aufgaben) + 1, "titel": titel, "erledigt": False}
    aufgaben.append(neue_aufgabe)

    return jsonify(neue_aufgabe), 201


if __name__ == "__main__":
    app.run(debug=True)
