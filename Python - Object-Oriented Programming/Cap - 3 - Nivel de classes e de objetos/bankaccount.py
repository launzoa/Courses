class BankAccount:
    
    interest_rate = 1.5
    population = 0
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        BankAccount.population+=1
    
    def __str__(self):
        return f"Nome: {self.name}, Saldo: {self.balance}, Juros: {BankAccount.interest_rate}"
    
    def interest_change(self, new_interest):
        BankAccount.interest_rate = new_interest
        
    def balance_increase(self, month):
        self.balance *= BankAccount.interest_rate * month
        return self.balance

    
