def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo {}".format(conta["saldo"]))

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto... {self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"Saldo de R${self.saldo} do titular {self.titular}")

    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        self.saldo -= valor
