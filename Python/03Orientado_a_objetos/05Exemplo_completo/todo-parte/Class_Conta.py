#Agregação parte 1
from Classe_Extrato import Extrato
class Conta:
    def __init__(self,clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.extrato = Extrato()
    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["Deposito", valor])
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["Saque", valor])
            return True