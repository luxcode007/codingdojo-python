class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()	# added this line
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)
        return self
    def display_user_balance(self):
        print(self.name, self.account.balance)
        return self

class BankAccount:
    bank_name = "Dojo Bank"
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        balance = 0
        int_rate = .005
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.balance, self.int_rate)
        return self
    def yield_interest(self):
        print(self.balance * self.int_rate)
        return self

# dojobank = BankAccount(.005, 500)
# codingcapital = BankAccount(.0075, 1000)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
lucky = User("Lucky Thompson", "lucky@python.com")

guido.account = BankAccount(.005, 500)
guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(50)
guido.make_withdrawal(150)
guido.display_user_balance()

monty.account = BankAccount(.0075, 1000)
monty.make_deposit(300)
monty.make_deposit(300)
monty.make_withdrawal(250)
monty.make_withdrawal(250)
monty.display_user_balance()

lucky.account = BankAccount(.003, 1500)
lucky.make_deposit(5000)
lucky.make_withdrawal(1000)
lucky.make_withdrawal(500)
lucky.make_withdrawal(3000)
lucky.display_user_balance()