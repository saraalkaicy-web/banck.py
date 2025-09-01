from methodes.account import Account
from methodes.deposit import Deposit
from methodes.transfer import Transfer
from methodes.withdraw import Withdraw

Customer_Account = {
    "sara": Account(224488, 700000, 1234),
    "Rawan": Account(556677, 500000, 2345),
    "mariam": Account(884400, 300000, 3456)
}   



name = input("Enter your name:")    
if name not in Customer_Account:
    print("wrong name")
else:
    PIN_Password = int(input("Enter your PIN/Password"))
    if PIN_Password != Customer_Account[name].PIN_Password:
        print("Wrong PIN/Password:")
    else:
        Deposit_amount = int(input("Enter amount to deposit:"))
        print(Deposit(Customer_Account[name], Deposit_amount).do_deposit())

        withdraw_amount = int (input("Enter amount to withdraw:"))
        print(Withdraw(Customer_Account[name], withdraw_amount).do_withdraw())
        to_name = input("Enter the name of the person you want to transfer to:")
        if to_name in Customer_Account:
            transfer_amount = int(input("Enter amount to transfer:"))
            print(Transfer(transfer_amount,Customer_Account[name], Customer_Account[to_name]).do_transfer())
        else:
            print("Recipient not Found")


