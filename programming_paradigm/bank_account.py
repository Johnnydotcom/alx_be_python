class BankAccount:
    
    def __init__(self, account_balance):
        self.account_balance = 0
        
    def deposit(self, amount):
        return self.account_balance + amount
    

    def withdraw(self, amount):
        return self.account_balance - amount
                    
    def dislpay_balance(self, amount):
        return()