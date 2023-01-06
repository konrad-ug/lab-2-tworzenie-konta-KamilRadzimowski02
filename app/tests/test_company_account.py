import unittest
from datetime import datetime

import app

from ..KontoFirmowe import KontoFirmowe
from unittest.mock import patch, MagicMock


class TestCompanyAccountCreation(unittest.TestCase):
    mock_nip = "0123456789"
    mock_co_name = "Essa sp.z.o"

    mock_too_short_nip = "012345678"
    mock_too_long_nip = "01234567891"

    @patch('app.KontoFirmowe.KontoFirmowe.govNipVerify')
    def test_company_account_creation(self, mock_czy_nip_istnieje_w_gov):
        mock_czy_nip_istnieje_w_gov.return_value = True

        mock_smtp_connection = MagicMock()
        mock_smtp_connection.wyslij.return_value = True

        konto_firmowe = KontoFirmowe(self.mock_co_name, self.mock_nip)
        self.assertEqual(konto_firmowe.balance, 0)
        self.assertEqual(konto_firmowe.nip, self.mock_nip)
        self.assertEqual(konto_firmowe.company_name, self.mock_co_name)
        self.assertEqual(konto_firmowe.isCompanyAccount, True)
        self.assertEqual(konto_firmowe.isPrivateAccount, False)

    @patch('app.KontoFirmowe.KontoFirmowe.govNipVerify')
    def test_company_account_too_short_nip(self, mock_czy_nip_istnieje_w_gov):
        mock_czy_nip_istnieje_w_gov.return_value = True
        konto_firmowe = KontoFirmowe(self.mock_co_name, self.mock_too_short_nip)
        self.assertEqual(konto_firmowe.nip, konto_firmowe.WRONG_NIP)

    @patch('app.KontoFirmowe.KontoFirmowe.govNipVerify')
    def test_company_account_too_long_nip(self, mock_czy_nip_istnieje_w_gov):
        mock_czy_nip_istnieje_w_gov.return_value = True
        konto_firmowe = KontoFirmowe(self.mock_co_name, self.mock_too_long_nip)
        self.assertEqual(konto_firmowe.nip, konto_firmowe.WRONG_NIP)

    @patch('app.KontoFirmowe.KontoFirmowe.govNipVerify')
    def test_company_account_not_in_gov(self, mock_czy_nip_istnieje_w_gov):
        mock_czy_nip_istnieje_w_gov.return_value = False
        konto_firmowe = KontoFirmowe(self.mock_co_name, self.mock_nip)
        self.assertEqual(konto_firmowe.nip, konto_firmowe.PRANIE_NIP)

    @patch('app.KontoFirmowe.KontoFirmowe.govNipVerify')
    def test_company_account_mail(self, mock_czy_nip_w_gov):
        mock_smtp_connection = MagicMock()
        mock_smtp_connection.wyslij.return_value = True

        mock_czy_nip_w_gov.return_value = True
        konto_firmowe = KontoFirmowe(self.mock_co_name, self.mock_nip)
        wasSend = konto_firmowe.wyslij_historie_na_maila("adresat", mock_smtp_connection)
        self.assertEqual(wasSend, True)

        date = datetime.today().strftime('%Y-%m-%d')
        temat = konto_firmowe.mail_title_string
        tresc = konto_firmowe.mail_content_string
        expected_title = f"{temat} {date}"
        expected_content = f"{tresc} {konto_firmowe.history}"
        mock_smtp_connection.wyslij.assert_called_once_with(expected_title, expected_content, "adresat")

    @patch('app.KontoFirmowe.KontoFirmowe.govNipVerify')
    def test_company_account_mail_not_send(self, mock_czy_nip_w_gov):
        mock_smtp_connection = MagicMock()
        mock_smtp_connection.wyslij.return_value = False

        mock_czy_nip_w_gov.return_value = True
        konto_firmowe = KontoFirmowe(self.mock_co_name, self.mock_nip)
        wasSend = konto_firmowe.wyslij_historie_na_maila("adresat", mock_smtp_connection)
        self.assertEqual(wasSend, False)

        date = datetime.today().strftime('%Y-%m-%d')
        temat = konto_firmowe.mail_title_string
        tresc = konto_firmowe.company_mail_content_string
        expected_title = f"{temat} {date}"
        expected_content = f"{tresc} {konto_firmowe.history}"
        mock_smtp_connection.wyslij.assert_called_once_with(expected_title, expected_content, "adresat")
