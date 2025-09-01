class Withdraw:
    def __init__(self, account, amount: float):
        self.account = account
        self.amount = amount

    def do_withdraw(self):
        if self.amount <= self.account.balance:
            self.account.balance -= self.amount
            return f"your balance is:{self.account.balance}"
        else:
            return "Insufficient funds"
