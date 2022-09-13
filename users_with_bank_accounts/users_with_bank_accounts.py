class BankAccount:
    def __init__(self):
        self.int_rate = 0
        self.balance = 0
        self.currency = "USD"
        self.type = "savings"

    def __init__(self, int_rate, balance, currency, type):
        self.int_rate = int_rate
        self.balance = balance
        self.currency = currency
        self.type = type

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.int_rate, self.balance, self.currency, self.type)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self


class User:
    def __init__(self, name, balance, currency, type, int_rate):
        self.name = name
        self.account = [BankAccount(int_rate, balance, currency, type)]

    def create_new_account(self, int_rate, balance, currency, type):
        self.account.append(BankAccount(int_rate, balance, currency, type))

    def make_deposit(self, account_num, amount):
        if account_num >= 0 and account_num < len(self.account):
            self.account[account_num].deposit(amount)
        else:
            print("Error: Account Doesn't Exist")
        return self

    def make_withdrawal(self, account_num, amount):
        if account_num >= 0 and account_num < len(self.account):
            self.account[account_num].withdraw(amount)
        else:
            print("Error: Account Doesn't Exist")
        return self

    def display_user_balance(self, account_num):
        if account_num >= 0 and account_num < len(self.account):
            print(self.name)
            self.account[account_num].display_account_info()
        else:
            print("Error: Account Doesn't Exist")
        return self

    def transfer_money(self, sender_account_num, user, reciever_account_num, amount):
        self.make_withdrawal(sender_account_num, amount)
        user.make_deposit(reciever_account_num, amount)
        return self


riyad = User("Riyad", 3000, "USD", "Savings", 0.02)
riyad.display_user_balance(0)
riyad.create_new_account(0.05, 5000, "NIS", "Savings")
riyad.display_user_balance(1)
riyad.display_user_balance(2)
riyad.create_new_account(0.066, 900, "JOD", "Savings")
riyad.display_user_balance(2)
riyad.display_user_balance(4)
riyad.create_new_account(0.08, 200, "EUR", "Savings")
riyad.display_user_balance(3)
riyad.create_new_account(0.05, 900, "JOD", "Main")
riyad.display_user_balance(4)


# riyad = User("Riyad", 500)
# amin = User("Amin", 2000)
# baraa = User("Baraa", 150000)

# riyad.make_deposit(500)
# riyad.make_deposit(2000)
# riyad.make_deposit(70000)
# riyad.make_withdrawal(500000)
# riyad.display_user_balance()

# amin.make_deposit(500)
# amin.make_deposit(500)
# amin.make_withdrawal(500)
# amin.make_withdrawal(500)
# amin.display_user_balance()

# baraa.make_deposit(500)
# baraa.make_withdrawal(500)
# baraa.make_withdrawal(500)
# baraa.make_withdrawal(500)
# baraa.display_user_balance()

# riyad.transfer_money(baraa, 300)
# riyad.display_user_balance()
# baraa.display_user_balance()