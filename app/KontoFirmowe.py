from .Konto import Konto


class KontoFirmowe(Konto):
    WRONG_NIP = "Niepoprawny NIP!"
    nip = ""
    company_name = ""

    def __init__(self, company_name, nip):
        super().__init__()

        self.isCompanyAccount = True
        self.company_name = company_name

        if verifyNip(nip):
            self.nip = nip
        else:
            self.nip = self.WRONG_NIP

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

def verifyNip(nip):
    return len(nip) == 10
