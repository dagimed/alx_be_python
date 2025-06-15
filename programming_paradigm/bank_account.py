class BankAccount:
    def __init__(self, acount_balance = 0.0):
        self.acount_balance = float(acount_balance)
    def deposit(self, amount):
        if amount > 0:
            self.acount_balance += amount
    def withdraw(self, amount):
        if 0< amount < self.acount_balance:
            self.acount_balance -= amount
            return True
        return False 
    def display_balance(self):
        print(f"Current Balance: ${self.acount_balance:.2f}")