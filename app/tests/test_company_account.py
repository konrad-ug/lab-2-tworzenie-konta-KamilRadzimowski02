import unittest

from ..KontoFirmowe import KontoFirmowe


class TestCompanyAccountCreation(unittest.TestCase):
    mock_nip = "0123456789"
    mock_co_name = "Essa sp.z.o"

    mock_too_short_nip = "012345678"
    mock_too_long_nip = "01234567891"

    def test_company_account_creation(self):
        konto_firmowe = KontoFirmowe(self.mock_co_name, self.mock_nip)
        self.assertEqual(konto_firmowe.balance, 0)
        self.assertEqual(konto_firmowe.nip, self.mock_nip)
        self.assertEqual(konto_firmowe.company_name, self.mock_co_name)
        self.assertEqual(konto_firmowe.isCompanyAccount, True)
        self.assertEqual(konto_firmowe.isPrivateAccount, False)

    def test_company_account_too_short_nip(self):
        konto_firmowe = KontoFirmowe(self.mock_co_name, self.mock_too_short_nip)
        self.assertEqual(konto_firmowe.nip, konto_firmowe.WRONG_NIP)

    def test_company_account_too_long_nip(self):
        konto_firmowe = KontoFirmowe(self.mock_co_name, self.mock_too_long_nip)
        self.assertEqual(konto_firmowe.nip, konto_firmowe.WRONG_NIP)