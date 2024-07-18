class BankAccount:
    
    def __init__(self, account_balance: float):
        self.account_balance = 0
        
    def deposit(self, amount):
        return self.account_balance + amount
    

    def withdraw(self, amount):
        if amount > self.account_balance:
            return True
        else:
            self.account_balance - amount
            return False
                    
    def display_balance(self, amount):
        return f"Current Balance: ${self.account_balance(amount)}"
