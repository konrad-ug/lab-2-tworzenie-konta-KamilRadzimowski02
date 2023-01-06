import unittest

from ..KontoPrywatne import KontoPrywatne
from ..KontoFirmowe import KontoFirmowe


class QuickExpressTest(unittest.TestCase):
    mock_name = "Dariusz"
    mock_surname = "Januszewski"
    mock_pesel = "12345678910"

    mock_co_name = "spółka zoooo"
    mock_nip = "0123456789"

    def test_quick_transfer(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel)
        konto.balance = 500

        konto.sendQuickTransfer(None, 500)
        self.assertEqual(konto.balance, -1)

    def test_quick_transfer_company_account(self):
        konto = KontoFirmowe(self.mock_co_name, self.mock_nip)
        konto.balance = 500

        konto.sendQuickTransfer(None, 500)
        self.assertEqual(konto.balance, -5)

    def test_quick_transfer_not_enough_money(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel)
        konto.balance = 500

        konto.sendQuickTransfer(None, 600)
        self.assertEqual(konto.balance, 500)

    def test_quick_transfer_company_account_not_enough_money(self):
        konto = KontoFirmowe(self.mock_co_name, self.mock_nip)
        konto.balance = 500

        konto.sendQuickTransfer(None, 600)
        self.assertEqual(konto.balance, 500)
