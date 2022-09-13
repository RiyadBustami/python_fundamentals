class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        print(self.name, self.balance)

    def transfer_money(self, user, amount):
        self.balance -= amount
        user.balance += amount


riyad = User("Riyad", 500)
amin = User("Amin", 2000)
baraa = User("Baraa", 150000)

riyad.make_deposit(500)
riyad.make_deposit(2000)
riyad.make_deposit(70000)
riyad.make_withdrawal(500000)
riyad.display_user_balance()

amin.make_deposit(500)
amin.make_deposit(500)
amin.make_withdrawal(500)
amin.make_withdrawal(500)
amin.display_user_balance()

baraa.make_deposit(500)
baraa.make_withdrawal(500)
baraa.make_withdrawal(500)
baraa.make_withdrawal(500)
baraa.display_user_balance()

riyad.transfer_money(baraa, 300)
riyad.display_user_balance()
baraa.display_user_balance()
