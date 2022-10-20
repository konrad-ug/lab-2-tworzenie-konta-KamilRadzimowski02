class Konto:
    WRONG_PESEL = "NIEPRAWIDLOWY_PESEL"

    imie = ""
    nazwisko = ""
    saldo = 0
    pesel = ""

    def __init__(self, name, surname, pesel):
        self.imie = name
        self.nazwisko = surname
        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = self.WRONG_PESEL
