class Bank:

    def __init__(self,accountholder,accountnumber,currency):
        self.accountholder=accountholder
        self.accountnumber=accountnumber
        self.currency=currency
        self.balance=0
        print(f"The new account with accountnumber,{self.accountnumber} is created for {self.accountholder}")
    def deposit(self):
        self.amount= float(input("Enter amount to be deposited: "))
        self.balance=self.balance+self.amount
        print(f"")
        print(f"Desposit is successful")
    def withdraw(self):
        self.amount=float(input("Enter the amount:"))
        self.balance=self.balance -self.amount
        print("Withdraw is successful")
    def enquiry(self):
        print(f"Balance on your account is {self.balance} {self.currency}")