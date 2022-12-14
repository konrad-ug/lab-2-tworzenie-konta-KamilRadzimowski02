from flask import Flask, request, jsonify
from .RejestrKont import RejestrKont
from .KontoPrywatne import KontoPrywatne

app = Flask(__name__)


@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = KontoPrywatne(dane["imie"], dane["nazwisko"], dane["pesel"])
    wasAdded = RejestrKont.add(konto)
    if wasAdded:
        return jsonify("Konto stworzone"), 201
    else:
        return jsonify("Pesel zajety"), 400


@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    # Twoja implementacja endpointu
    return jsonify(count=RejestrKont.count())


@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    # Twoja implementacja endpointu
    konto = RejestrKont.find(pesel)
    if konto is None:
        return jsonify(imie=None, nazwisko=None, pesel=None), 200
    else:
        return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel), 200


@app.route("/konta/update/<pesel>/<nazwisko>", methods=['POST'])
def update_konto(pesel, nazwisko):
    RejestrKont.update(nazwisko, pesel)
    return jsonify("ok"), 200


@app.route("/konta/konto/delete/<pesel>", methods=['DELETE'])
def delete_konto(pesel):
    RejestrKont.delete(pesel)
    return jsonify("deleted"), 200


@app.route("/konta/clear", methods=['DELETE'])
def clear():
    RejestrKont.list = []
    return jsonify("cleared"), 200
