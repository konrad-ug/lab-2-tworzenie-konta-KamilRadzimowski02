import unittest

from ..KontoPrywatne import KontoPrywatne
from ..RejestrKont import RejestrKont


class AccountListTest(unittest.TestCase):
    pesel = "01234567890"
    not_used_pesel = "999999999"
    konto = KontoPrywatne("test", "test", pesel)

    def setUp(self):
        self.rejestr = RejestrKont()

    def test_add_account(self):
        self.assertEqual(self.rejestr.list, [])

        self.rejestr.add(self.konto)

        self.assertEqual(self.rejestr.list, [self.konto])

    def test_count(self):
        self.assertEqual(self.rejestr.count(), 1)

    def test_find(self):
        self.assertEqual(self.rejestr.find(self.pesel), self.konto)

    def test_find_not_found(self):
        self.assertEqual(self.rejestr.find(self.not_used_pesel), None)
