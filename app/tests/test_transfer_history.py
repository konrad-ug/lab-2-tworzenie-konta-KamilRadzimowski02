import unittest

from ..KontoPrywatne import KontoPrywatne


class TestTransfer(unittest.TestCase):
    mock_name = "Dariusz"
    mock_surname = "Januszewski"
    mock_pesel = "12345678910"

    def test_history(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel)
        konto.balance = 500

        receiver = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel)

        konto.sendTransfer(receiver, 500)
        self.assertEqual(konto.history, [-500])

        konto.receiveTransfer(300)
        self.assertEqual(konto.history, [-500, 300])

    def test_history_quick_transfer(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel)
        konto.balance = 500

        receiver = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel)

        konto.sendQuickTransfer(receiver, 500)
        self.assertEqual(konto.history, [-500])

        konto.receiveTransfer(300)
        self.assertEqual(konto.history, [-500, 300])

    def test_history_transfer_not_sent(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel)
        konto.balance = 500

        receiver = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel)
        konto.sendTransfer(receiver, 1000)

        self.assertEqual(konto.history, [])

    def test_empty_history(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel)
        self.assertEqual(konto.history, [])
