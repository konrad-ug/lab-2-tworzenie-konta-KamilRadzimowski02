import unittest

from parameterized import parameterized

from ..KontoPrywatne import KontoPrywatne
from ..KontoFirmowe import KontoFirmowe


class TakeLoanTest(unittest.TestCase):
    mock_name = "Dariusz"
    mock_surname = "Januszewski"
    mock_nip = "0123456789"

    def setUp(self):
        self.konto = KontoPrywatne(self.mock_name, self.mock_surname,  self.mock_nip)
        self.kontoFirmowe = KontoFirmowe(self.mock_name, self.mock_nip)

    @parameterized.expand([
        ([300, 300, 300], 500, True, 500),
        ([], 500, False, 0),
        ([300, 300], 800, False, 0),
        ([-200, 200, 200], 500, False, 0),
        ([500, -200, 300, -200, 1000], 500, True, 500),
        ([500, -200, 300, -200, 1000], 2500, False, 0)
    ])
    def test_borrow_private_account(self, history, loan_amount, expected_result, expected_balance):
        self.konto.history = history

        was_money_lend = self.konto.borrow(loan_amount)

        self.assertEqual(was_money_lend, expected_result)
        self.assertEqual(self.konto.balance, expected_balance)

    @parameterized.expand([
        ([300, 300, -1775], 1000, 500, True, 1500),
        ([300, 300, -1775], 900, 500, False, 900),
        ([300, 300], 900, 500, False, 900),
        ([300, 300, 900], 1000, 500, False, 1000),
    ])
    def test_borrow_company_account(self, history, balance, loan_amount, expected_result, expected_balance):
        self.kontoFirmowe.history = history
        self.kontoFirmowe.balance = balance

        was_money_lend = self.kontoFirmowe.borrow(loan_amount)

        self.assertEqual(was_money_lend, expected_result)
        self.assertEqual(self.kontoFirmowe.balance, expected_balance)


