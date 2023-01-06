import requests

from .Konto import Konto
from datetime import datetime

BANK_APP_MF_URL = "https://wl-api.mf.gov.pl"


class KontoFirmowe(Konto):
    WRONG_NIP = "Niepoprawny NIP!"
    PRANIE_NIP = "PRANIE!"
    nip = ""
    company_name = ""

    company_mail_content_string = "Historia konta twojej firmy to:"

    def __init__(self, company_name, nip):
        super().__init__()

        self.isCompanyAccount = True
        self.mail_content_string = self.company_mail_content_string
        self.company_name = company_name

        if verifyNip(nip):
            self.nip = nip
        else:
            self.nip = self.WRONG_NIP
        if not self.govNipVerify(nip):
            self.nip = self.PRANIE_NIP

    def contains_zus_transaction(self):
        result = False
        for entry in self.history:
            if entry == -1775:
                result = True
        return result

    def borrow(self, amount):
        if self.balance >= (amount * 2) and self.contains_zus_transaction():
            self.balance += amount
            return True
        else:
            return False

    def govNipVerify(self, nip):
        date = datetime.today().strftime('%Y-%m-%d')
        r = requests.get(f"{BANK_APP_MF_URL}/api/search/nip/{nip}?{date}", json={})
        return r.status_code == 200


def verifyNip(nip):
    return len(nip) == 10



