class BankAccount:
    def __init__(self,int_rate = 0.01,balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        self.balance -= amount
        if self.balance <0:
            print("insufficient funds:charging a $5 fee")
            self.balance = -5
        return self
    def display_account_info(self):
        print(self.balance)
    def yield_interest(self):
        if self.balance < 0:
            return self
        self.balance =  self.balance + (self.balance * self.int_rate)
        return self

first_account= BankAccount(0.05,500)
second_account= BankAccount(0.03,100)

first_account.deposit(100).deposit(200).deposit(100).withdraw(200).yield_interest().display_account_info()
second_account.deposit(200).deposit(400).withdraw(200).withdraw(100).withdraw(300).withdraw(150).yield_interest().display_account_info()
