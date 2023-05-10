class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)


Muntaser = User('Muntaser Younis','muntaserdagher@gmail.com')
Shatha = User('Shat-ha Bast','shatha@bast.com')
Khalid = User('Khalid Khader','khalid@khader.com')
# Update your previous assignment so that each instance's methods are chained
Muntaser.make_deposit(100).make_deposit(200).make_deposit(250).display_user_balance()
Shatha.make_deposit(1000).make_deposit(10000).make_withdrawal(200).make_withdrawal(5000).display_user_balance()
Khalid.make_deposit(1000).make_withdrawal(500).make_withdrawal(400).make_withdrawal(100).display_user_balance()

