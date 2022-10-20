import re

class Konto:
    WRONG_PESEL = "NIEPRAWIDLOWY_PESEL"

    code_pattern = re.compile("^PROM_[A-Z][A-Z][A-Z]$")
    code_bonus = 50

    imie = ""
    nazwisko = ""
    saldo = 0
    pesel = ""


    def __init__(self, name, surname, pesel, code = None):
        self.imie = name
        self.nazwisko = surname

        # Validate PESEL
        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = self.WRONG_PESEL

        # Validate discount code

        if code is not None:
            if self.code_pattern.match(code):
                self.saldo = self.code_bonus


