import unittest

import app

from ..KontoFirmowe import KontoFirmowe
from unittest.mock import patch


class TestCompanyAccountCreation(unittest.TestCase):
    mock_nip = "0123456789"
    mock_co_name = "Essa sp.z.o"

    mock_too_short_nip = "012345678"
    mock_too_long_nip = "01234567891"

    @patch('app.KontoFirmowe.KontoFirmowe.govNipVerify')
    def test_company_account_creation(self, mock_czy_nip_istnieje_w_gov):
        mock_czy_nip_istnieje_w_gov.return_value = True

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
