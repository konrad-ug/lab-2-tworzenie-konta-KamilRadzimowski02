import unittest

from ..KontoPrywatne import KontoPrywatne


class TestTransfer(unittest.TestCase):
    mock_name = "Dariusz"
    mock_surname = "Januszewski"
    mock_pesel = "12345678910"

    def test_transfer_receive(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel)
        self.assertEqual(konto.balance, 0)

        konto.receiveTransfer(500)

        self.assertEqual(konto.balance, 500)

    def test_transfer_send(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel)
        konto.balance = 1000
        receiver = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel)

        wasSent = konto.sendTransfer(receiver, 600)

        self.assertEqual(konto.balance, 400)
        self.assertEqual(wasSent, True)

    def test_transfer_send_not_enough_money(self):
        konto = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel)
        konto.balance = 200
        receiver = KontoPrywatne(self.mock_name, self.mock_surname, self.mock_pesel)

        wasSent = konto.sendTransfer(receiver, 600)

        self.assertEqual(konto.balance, 200)
        self.assertEqual(wasSent, False)