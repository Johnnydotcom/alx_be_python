class BankAccount:
    def __init__(self, account_balance: float):
        self.current_balance = account_balance
        
    def deposit(self, amount):
        return self.current_balance + amount
    

    def withdraw(self, amount):
        if amount > self.current_balance:
            return False
        else:
            self.current_balance - amount
            return True
                    
    def display_balance(self, amount):
        return f"Current Balance: {self.current_balance(amount)}"
