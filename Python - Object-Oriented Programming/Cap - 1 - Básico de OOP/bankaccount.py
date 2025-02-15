class BankAccount:
    
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        
    def deposit(self, deposito):
        self.saldo += deposito
    
    def withdraw(self, saque):
        if(saque > self.saldo):
            print("Não é possível sacar, valor disponível inferior ao desejado")
        else:
            self.saldo -= saque
            
    def __str__(self):
        return f"Nome: {self.nome}, Saldo: {self.saldo}"