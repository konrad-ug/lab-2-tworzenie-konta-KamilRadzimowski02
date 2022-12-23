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

    private_mail_content_string = "Twoja historia konta to:"

    imie = ""
    nazwisko = ""
    pesel = ""

    def __init__(self, name, surname, pesel, code=None):
        super().__init__()

        self.mail_content_string = self.private_mail_content_string
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

    def borrow(self, amount):
        if self.are_3_last_history_items_bigger_than_zero() or self.is_sum_of_last_5_transactions_bigger_than_loan(
                amount):
            self.balance += amount
            return True
        else:
            return False

    def is_sum_of_last_5_transactions_bigger_than_loan(self, amount):
        if len(self.history) >= 5:
            sum_of_5 = 0
            for item in self.history[-5:]:
                sum_of_5 += item
            return sum_of_5 > amount
        else:
            return False

    def are_3_last_history_items_bigger_than_zero(self):
        if len(self.history) >= 3:
            for item in self.history[-3:]:
                if item < 0:
                    return False
            return True
        else:
            return False
