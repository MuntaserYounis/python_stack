class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02,balance=0)
    def make_deposit(self, amount):
        self.account.deposit += amount
    def make_withdrawal(self, amount):
        self.account.withdraw -= amount
    def display_user_balance(self):
        print(self.account.display_account_info())

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

Muntaser = User('Muntaser Younis','muntaserdagher@gmail.com')
Muntaser.account.deposit(100)
Muntaser.display_user_balance()