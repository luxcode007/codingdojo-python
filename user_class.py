# User Class excersize

class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.name, self.account_balance)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
lucky = User("Lucky Thompson", "lucky@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(50)
guido.make_withdrawal(150)
guido.display_user_balance()

monty.make_deposit(300)
monty.make_deposit(300)
monty.make_withdrawal(250)
monty.make_withdrawal(250)
monty.display_user_balance()

lucky.make_deposit(5000)
lucky.make_withdrawal(1000)
lucky.make_withdrawal(500)
lucky.make_withdrawal(3000)
lucky.display_user_balance()

#  Class Answers

class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()

adrien = User("Adrien")
nibbles = User("Mr. Nibbles")
benny_bob = User("Benny Bob")

# transfer money instance

nibbles.transfer_money(400, adrien)