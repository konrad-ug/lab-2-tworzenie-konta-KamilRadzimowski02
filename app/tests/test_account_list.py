import unittest

from ..KontoPrywatne import KontoPrywatne
from ..RejestrKont import RejestrKont


class AccountListTest(unittest.TestCase):
    pesel = "01234567890"
    pesel2 = "01234567891"
    not_used_pesel = "999999999"
    konto = KontoPrywatne("test", "test", pesel)
    konto2 = KontoPrywatne("test2", "test2", pesel2)

    def setUp(self):
        self.rejestr = RejestrKont()

    def test_add_account(self):

        self.rejestr.add(self.konto)

        self.assertEqual(self.rejestr.list, [self.konto])

    def test_count(self):
        self.assertEqual(self.rejestr.count(), 1)

    def test_find(self):
        self.assertEqual(self.rejestr.find(self.pesel), self.konto)

    def test_find_not_found(self):
        self.assertEqual(self.rejestr.find(self.not_used_pesel), None)

    def test_account_exists(self):
        self.rejestr.add(self.konto)
        result = self.rejestr.add(self.konto)
        self.assertEqual(result, False)

    def test_account_delete(self):
        self.rejestr.add(self.konto)
        self.rejestr.add(self.konto2)
        self.rejestr.delete(self.konto2.pesel)
        self.assertEqual(self.rejestr.list, [self.konto])

    @classmethod
    def tearDownClass(cls):
        RejestrKont.list = []
