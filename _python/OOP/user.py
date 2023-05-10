class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)


Muntaser = User('Muntaser Younis','muntaserdagher@gmail.com')
Shatha = User('Shat-ha Bast','shatha@bast.com')
Khalid = User('Khalid Khader','khalid@khader.com')

Muntaser.make_deposit(100)
Muntaser.make_deposit(200)
Muntaser.make_deposit(250)
Muntaser.display_user_balance()

Shatha.make_deposit(1000)
Shatha.make_deposit(10000)
Shatha.make_withdrawal(200)
Shatha.make_withdrawal(5000)
Shatha.display_user_balance()

Khalid.make_deposit(1000)
Khalid.make_withdrawal(500)
Khalid.make_withdrawal(400)
Khalid.make_withdrawal(100)
Khalid.display_user_balance()
