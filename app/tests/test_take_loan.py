import unittest

from ..KontoFirmowe import KontoFirmowe


class TakeLoanTest(unittest.TestCase):
    mock_name = "Dariusz"
    mock_surname = "Januszewski"
    mock_nip = "0123456789"

    def setUp(self):
        self.konto = KontoFirmowe(self.mock_name, self.mock_nip)

    def test_3_ostatnie_transakcje_to_wplaty(self):
        self.konto.history = [300, 300, 300]

        was_money_lend = self.konto.borrow(500)

        self.assertEqual(was_money_lend, True)
        self.assertEqual(self.konto.balance, 500)

    def test_loan_no_history(self):
        was_money_lend = self.konto.borrow(500)

        self.assertEqual(was_money_lend, False)
        self.assertEqual(self.konto.balance, 0)

    def test_loan_history_not_enough_transactions(self):
        self.konto.history = [300, 300]

        was_money_lend = self.konto.borrow(800)

        self.assertEqual(was_money_lend, False)
        self.assertEqual(self.konto.balance, 0)

    def test_loan_history_with_negative_transaction(self):
        self.konto.history = [-200, 200, 200]

        was_money_lend = self.konto.borrow(500)

        self.assertEqual(was_money_lend, False)
        self.assertEqual(self.konto.balance, 0)

    def test_sum_of_5_transactions_bigger_than_loan(self):
        self.konto.history = [500, -200, 300, -200, 1000]

        was_money_lend = self.konto.borrow(500)

        self.assertTrue(was_money_lend)
        self.assertEqual(self.konto.balance, 500)

    def test_sum_of_5_transactions_smaller_than_loan(self):
        self.konto.history = [500, -200, 300, -200, 1000]

        was_money_lend = self.konto.borrow(2500)

        self.assertEqual(was_money_lend, False)
        self.assertEqual(self.konto.balance, 500)



