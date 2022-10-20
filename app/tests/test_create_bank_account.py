import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    mock_name = "Dariusz"
    mock_surname = "Januszewski"
    mock_pesel = "12345678910"
    starting_balance = 0

    mock_too_short_pesel = "123"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.mock_name, self.mock_surname, self.mock_pesel)
        self.assertEqual(pierwsze_konto.imie, self.mock_name, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.mock_surname, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, self.starting_balance, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.mock_pesel, "Nieprawidłowy pesel")

    def test_tworzenie_konta_nieprawidlowy_pesel(self):
        konto = Konto(self.mock_name, self.mock_surname, self.mock_too_short_pesel)
        self.assertEqual(konto.pesel, konto.WRONG_PESEL, "Brak informacji o zlym peselu")
