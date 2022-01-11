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

dojobank = BankAccount(.005, 500)
codingcapital = BankAccount(.0075, 1000)

dojobank.deposit(500).deposit(1000).deposit(500).withdraw(500).yield_interest().display_account_info()

codingcapital.deposit(500).deposit(1000).withdraw(250).withdraw(150).withdraw(250).withdraw(500).yield_interest().display_account_info()

