class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def get_account_number(self):
        return self.account_number
    def get_balance(self):
        return self.balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(amount, "deposited successfully")
        else:
            print("Invalid amount for deposit")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully")
        else:
            print("Insufficient balance")
# Object creation
account = BankAccount("123456789", 1000)
print("Account number:", account.get_account_number())
print("Balance:", account.get_balance())
account.deposit(500)
account.withdraw(300)
print("Final balance:", account.get_balance())
