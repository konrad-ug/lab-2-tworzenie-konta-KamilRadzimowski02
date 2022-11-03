import re

from .Konto import Konto

def getYearOfBirthBasedOnPesel(pesel):
    year = pesel[:2]
    century_encoded = pesel[2:4]
    # This person was born before 1900
    if int(century_encoded) > 80:
        return f"18{year}"
    elif int(century_encoded) > 20:
        return f"20{year}"
    else:
        return f"19{year}"



def validatePesel(pesel):
    return len(pesel) == 11


class KontoPrywatne(Konto):
    WRONG_PESEL = "NIEPRAWIDLOWY_PESEL"

    code_pattern = re.compile("^PROM_[A-Z][A-Z][A-Z]$")
    code_bonus = 50
    code_birth_year = 1960

    imie = ""
    nazwisko = ""
    pesel = ""


    def __init__(self, name, surname, pesel, code = None):
        super().__init__()

        self.isPrivateAccount = True
        self.imie = name
        self.nazwisko = surname

        if validatePesel(pesel):
            self.pesel = pesel
        else:
            self.pesel = self.WRONG_PESEL

        # Validate discount code

        if code is not None:
            year = getYearOfBirthBasedOnPesel(pesel)
            if self.code_pattern.match(code) and int(year) > 1960:
                self.balance = self.code_bonus


