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


def verifyNip(nip):
    return len(nip) == 10
