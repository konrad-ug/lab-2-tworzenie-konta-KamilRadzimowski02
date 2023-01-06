from datetime import datetime


class Konto:
    balance = 0
    history = []
    isCompanyAccount = False
    isPrivateAccount = False

    mail_title_string = "Wyciąg z dnia:"
    mail_content_string = ""

    companyAccountPrice = 5
    personalAccountPrice = 1

    def __init__(self):
        self.history = []
        self.balance = 0
        pass

    def receiveTransfer(self, amount):
        self.balance += amount
        self.history.append(amount)

    def sendTransfer(self, receiver, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            self.history.append(amount * -1)
            return True
        else:
            return False

    def sendQuickTransfer(self, receiver, amount):
        if self.isPrivateAccount:
            price = self.personalAccountPrice
        else:
            price = self.companyAccountPrice

        if self.balance >= amount:
            self.balance = self.balance - amount - price
            self.history.append(amount * -1)
            return True
        else:
            return False

    def wyslij_historie_na_maila(self, adresat, connection):
        date = datetime.today().strftime('%Y-%m-%d')
        temat = f"{self.mail_title_string} {date}"
        tresc = f"{self.mail_content_string} {self.history}"
        return connection.wyslij(temat, tresc, adresat)

