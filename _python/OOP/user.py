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
    def transfer(self, amount, another_user):
        self.make_withdrawal(amount)
        another_user.make_deposit(amount)
        self.display_user_balance()


Muntaser = User('Muntaser Younis','muntaserdagher@gmail.com')
Muntaser.display_user_balance()
Shatha = User('Shat-ha Bast','shatha@bast.com')
Khalid = User('Khalid Khader','khalid@khader.com')
# Have the first user make 3 deposits and 1 withdrawal and then display their balance
Muntaser.make_deposit(100)
Muntaser.make_deposit(200)
Muntaser.make_deposit(250)
Muntaser.display_user_balance()
# Have the second user make 2 deposits and 2 withdrawals and then display their balance
Shatha.make_deposit(1000)
Shatha.make_deposit(10000)
Shatha.make_withdrawal(200)
Shatha.make_withdrawal(5000)
Shatha.display_user_balance()
# Have the third user make 1 deposits and 3 withdrawals and then display their balance
Khalid.make_deposit(1000)
Khalid.make_withdrawal(500)
Khalid.make_withdrawal(400)
Khalid.make_withdrawal(100)
Khalid.display_user_balance()

Muntaser.transfer(549,Shatha)
Shatha.display_user_balance()
