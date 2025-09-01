class Account:
    def __init__(self, accunt_number: int, balance: float, PIN_Password: int ):
        self.accunt_number = accunt_number
        self.balance = balance
        self.PIN_Password = PIN_Password

    def getinfo(self):
        return f"Accunt Number: {self.accunt_number}, Balance: {self.balance}, PIN/Password: {self.PIN_Password}"


