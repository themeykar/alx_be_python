class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance


    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited ${amount}. Current Balance: ${self.account_balance}")

        else:
            print("Deposit amount must be a positive number")

    def withdraw(self, amount):
        if amount <= 0:
            print("withdrawal amount must be a positive number")
            return False

        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew ${amount}. Current Balance: ${self.account_balance}")
            return True
        else:
            print(f"Insufficient funds. Current balance: ${self.account_balance}")
            return False


    def display_balance(self):
        print(f"Available Balance: ${self.account_balance}")



