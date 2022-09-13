class BankAccount:
    def __init__(self):
        self.int_rate = 0
        self.balance = 0

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.int_rate, self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self


account1 = BankAccount(0.03, 300)
account2 = BankAccount(0.1, 100_000)

account1.deposit(100).deposit(200).deposit(300).withdraw(
    150
).yield_interest().display_account_info()

account2.deposit(5000).deposit(2000).withdraw(300).withdraw(150).withdraw(200).withdraw(
    100
).yield_interest().display_account_info()
