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

    def borrow(self, amount):
        if self.are_3_last_history_items_bigger_than_zero() or self.is_sum_of_last_5_transactions_bigger_than_loan(amount):
            self.balance += amount
            return True
        else:
            return False

    def is_sum_of_last_5_transactions_bigger_than_loan(self, amount):
        if len(self.history) >= 5:
            sum_of_5 = 0
            for item in self.history[-5:]:
                sum_of_5 += item
            return sum_of_5 > amount
        else:
            return False

    def are_3_last_history_items_bigger_than_zero(self):
        if len(self.history) >= 3:
            for item in self.history[-3:]:
                if item < 0:
                    return False
            return True
        else:
            return False
