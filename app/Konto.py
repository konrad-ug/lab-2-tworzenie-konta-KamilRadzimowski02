class Konto:
    balance = 0
    isCompanyAccount = False
    isPrivateAccount = False

    companyAccountPrice = 5
    personalAccountPrice = 1

    def __init__(self):
        pass

    def receiveTransfer(self, amount):
        self.balance += amount

    def sendTransfer(self, receiver, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
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
            return True
        else:
            return False
