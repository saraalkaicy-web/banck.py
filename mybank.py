class Account:
    def __init__(self, accunt_number, balance, PIN_Password):
        self.accunt_number = accunt_number
        self.balance = balance
        self.PIN_Password = PIN_Password

    def getinfo(self):
        return f"Account Number: {self.accunt_number}, Balance: {self.balance}, PIN/Password: {self.PIN_Password}"    

Customer_Account = {
    "sara": Account(224488, 700000, 1234),
    "Rwan": Account(556677, 500000, 2345),
    "mariam": Account(884400, 300000, 3456)
}


def Deposit(name, amount):
    if name in Customer_Account:
        Customer_Account[name].balance += amount
        return f"your balance is: {Customer_Account[name].balance}"

def withdeaw(name, amount):
    if name in Customer_Account:
        if amount <= Customer_Account[name].balance:
            Customer_Account[name].balance -= amount
            return f"your balance is: {Customer_Account[name].balance}"

def transfer(name, amount, to_name):
    if name in Customer_Account and to_name in Customer_Account:
        if amount <= Customer_Account[name].balance:
            Customer_Account[name].balance -= amount
            Customer_Account[name].balance += amount
            return f"your balance is: {Customer_Account[name].balance}"
        
name = input("Enter your name:")
if name in Customer_Account:
    password = int(input("Enter your PIN/Password:"))
    if password == Customer_Account[name].PIN_Password:
        print(Account.getinfo(Customer_Account[name]))
    else:
        print("Incorrect PIN/Password.")
Deposit_amount = int(input("Enter amount to deposit:"))
print(Deposit(name, Deposit_amount))
withdeaw_amount = int(input("Enter amount to Withdeaw:"))
print(withdeaw(name, withdeaw_amount))
to_name = (input("Enter the name of the person you want "))
transfer_amount = int(input("Enter amount to transfer:"))
print(transfer(name, transfer_amount, to_name))