class Transfer:
    def __init__(self, amount: float, from_account, to_account):
        self.amount = amount
        self.from_account = from_account
        self.to_account = to_account

    def do_transfer(self):
        if self.amount <= self.from_account.balance:
            self.from_account.balance -= self.amount
            self.to_account.balance += self.amount
            return f"Transfer Done, your new balance is: {self.from_account.balance}"
        else:
            return "Insufficint funds"


        