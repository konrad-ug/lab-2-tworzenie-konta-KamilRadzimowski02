import unittest

from parameterized import parameterized

from ..KontoPrywatne import KontoPrywatne


class TakeLoanTest(unittest.TestCase):
    mock_name = "Dariusz"
    mock_surname = "Januszewski"
    mock_nip = "0123456789"

    def setUp(self):
        self.konto = KontoPrywatne(self.mock_name, self.mock_surname,  self.mock_nip)

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


