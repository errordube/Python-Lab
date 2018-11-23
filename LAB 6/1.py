class BankAccount(object):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
my_account = BankAccount(15)
my_account.withdraw(5)
print(my_account.balance)
        
