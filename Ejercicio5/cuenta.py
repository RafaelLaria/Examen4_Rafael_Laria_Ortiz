class Cuenta:
    def __init__(self, titular, iban, saldo = 0.0):
        self.titular = titular
        self.iban = iban
        self.saldo = saldo
    
    def __str__(self):
        return f'IBAN: {self.iban}\n' \
               f'TITULAR: {self.titular}\n' \
               f'SALDO: {self.saldo}'
    def ingresar(self, cantidad):
        self.saldo += cantidad
    def retirar(self, cantidad):
        if cantidad < self.saldo:
            self.saldo -= cantidad
            print(self.saldo)
        else:
            print('Saldo insuficiente')
    