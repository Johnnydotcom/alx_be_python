class BankAccount:
    #account_balance = 0.00
    def __init__(self, account_balance):
        self.account_balance = account_balance
        
    def deposit(self, amount):
        return self.account_balance + amount
    

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        elif amount <= self.account_balance:
            self.account_balance - amount
            return True
                    
    def display_balance(self):
        print(f"Current Balance: ${format(self.account_balance,".2f")}")
