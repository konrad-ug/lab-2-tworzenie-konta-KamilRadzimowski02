class Konto:
    balance = 0
    history = []
    isCompanyAccount = False
    isPrivateAccount = False

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

