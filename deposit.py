class Deposit:
    def __init__(self, account, amount: float):
        self.account = account
        self.amount = amount

    def do_deposit(self):
        self.account.balance += self.amount
        return f"your balance is: {self.account.balance}"    
