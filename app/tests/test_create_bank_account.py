import unittest
from datetime import datetime

from ..KontoPrywatne import KontoPrywatne
from unittest.mock import MagicMock


class TestCreateBankAccount(unittest.TestCase):
    mock_name = "Dariusz"
    mock_surname = "Januszewski"
    mock_pesel = "12345678910"
    mock_pesel_2002 = "02272101034"
    mock_pesel_1980 = "80122101034"
    mock_pesel_1959 = "59122101034"
    mock_pesel_1898 = "98842101034"
    mock_discount_code = "PROM_XYZ"
    starting_balance = 0
    starting_balance_with_code = 50

    mock_too_short_pesel = "123"
    mock_pesel_too_old_for_promo_code = "55864356781"

    mock_invalid_discount_code_no_suffix = "PROM"
    mock_invalid_discount_code_no_prefix = "XYZ"
    mock_invalid_discount_code_wrong_prefix = "STH_XYZ"
    mock_invalid_discount_code_wrong_suffix = "PROM_AAAA"
    mock_invalid_discount_code_string_in_the_middle = "STHPROM_XYZSTH"

    def test_tworzenie_konta_bez_rabatu(self):
        pierwsze_konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel)
        self.assertEqual(pierwsze_konto.imie, self.mock_name, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.mock_surname, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.balance, self.starting_balance, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.mock_pesel, "Nieprawidłowy pesel")
        self.assertEqual(pierwsze_konto.isCompanyAccount, False)
        self.assertEqual(pierwsze_konto.isPrivateAccount, True)

    def test_tworzenie_konta_nieprawidlowy_pesel(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_too_short_pesel)
        self.assertEqual(konto.pesel, konto.WRONG_PESEL, "Brak informacji o zlym peselu")

    def test_tworzenie_konta_z_kodem_rabatowym(self):
        konto_z_kodem = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel, self.mock_discount_code)
        self.assertEqual(konto_z_kodem.balance, self.starting_balance_with_code,
                         "Saldo nie uleglo zmianie po dodaniu kodu")

    def test_tworzenie_konta_z_nieprawidlowym_kodem_no_suffix(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel,
                              self.mock_invalid_discount_code_no_suffix)
        self.assertEqual(konto.balance, self.starting_balance, "Saldo uleglo zmianie mimo zlego kodu: brak suffixu")

    def test_tworzenie_konta_z_nieprawidlowym_kodem_no_prefix(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel,
                              self.mock_invalid_discount_code_no_prefix)
        self.assertEqual(konto.balance, self.starting_balance, "Saldo uleglo zmianie mimo zlego kodu: brak prefixu")

    def test_tworzenie_konta_z_nieprawidlowym_kodem_wrong_suffix(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel,
                              self.mock_invalid_discount_code_wrong_suffix)
        self.assertEqual(konto.balance, self.starting_balance, "Saldo uleglo zmianie mimo zlego kodu: zly suffix")

    def test_tworzenie_konta_z_nieprawidlowym_kodem_wrong_prefix(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel,
                              self.mock_invalid_discount_code_wrong_prefix)
        self.assertEqual(konto.balance, self.starting_balance, "Saldo uleglo zmianie mimo zlego kodu: zly prefix")

    def test_tworzenie_konta_z_nieprawidlowym_kodem_string_in_the_middle(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel,
                              self.mock_invalid_discount_code_string_in_the_middle)
        self.assertEqual(konto.balance, self.starting_balance,
                         "Saldo uleglo zmianie mimo zlego kodu: dobry string wew. innego")

    def test_tworzenie_konta_z_kodem_zbyt_stara_data(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel_too_old_for_promo_code,
                              self.mock_discount_code)
        self.assertEqual(konto.balance, self.starting_balance, "Saldo uległo zmianie mimo zbyt duzego wieku")

    def test_tworzenie_konta_z_kodem_osoba_urodzona_po_2000(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel_2002, self.mock_discount_code)
        self.assertEqual(konto.balance, self.starting_balance_with_code, f"Saldo nie uległo zmianie mimo dobrego kodu, "
                                                                         f"Konto: ${konto}")

    def test_tworzenie_konta_z_kodem_osoba_urodzona_przed_1899(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel_1898, self.mock_discount_code)
        self.assertEqual(konto.balance, self.starting_balance, "Saldo uległo zmianie mimo zbyt dużego wieku")

    def test_tworzenie_konta_z_kodem_osoba_urodzona_w_1980(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel_1980, self.mock_discount_code)
        self.assertEqual(konto.balance, self.starting_balance_with_code, f"Saldo nie uległo zmianie mimo dobrego kodu, "
                                                                         f"Konto: ${konto}")

    def test_wysylanie_maila(self):
        mock_smtp_connection = MagicMock()
        mock_smtp_connection.wyslij.return_value = True

        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel_1980)
        wasSend = konto.wyslij_historie_na_maila("adresat", mock_smtp_connection)
        self.assertEqual(wasSend, True)

        date = datetime.today().strftime('%Y-%m-%d')
        temat = konto.mail_title_string
        tresc = konto.mail_content_string
        expected_title = f"{temat} {date}"
        expected_content = f"{tresc} {konto.history}"
        mock_smtp_connection.wyslij.assert_called_once_with(expected_title, expected_content, "adresat")

    def test_wysylanie_maila_niepowodzenie(self):
        mock_smtp_connection = MagicMock()
        mock_smtp_connection.wyslij.return_value = False

        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel_1980)
        wasSend = konto.wyslij_historie_na_maila("adresat", mock_smtp_connection)
        self.assertEqual(wasSend, False)

        date = datetime.today().strftime('%Y-%m-%d')
        temat = konto.mail_title_string
        tresc = konto.mail_content_string
        expected_title = f"{temat} {date}"
        expected_content = f"{tresc} {konto.history}"
        mock_smtp_connection.wyslij.assert_called_once_with(expected_title, expected_content, "adresat")

