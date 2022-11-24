from flask import Flask, request, jsonify
from .RejestrKont import RejestrKont
from .KontoPrywatne import KontoPrywatne

app = Flask(__name__)


@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = KontoPrywatne(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.add(konto)
    return jsonify("Konto stworzone"), 201


@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    # Twoja implementacja endpointu
    return jsonify(count=RejestrKont.count())


@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    # Twoja implementacja endpointu
    dane = request.get_json()
    konto = RejestrKont.find(dane["pesel"])
    return jsonify(imie=konto.imie, nazwisko=konto.surname, pesel=konto.pesel), 200
