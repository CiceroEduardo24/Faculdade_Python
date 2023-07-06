# Tipos de associação entre objetos
# 01Agregação
import datetime
from Extrato import *


class Conta:
    def __init__(self, cliente, numero, saldo):
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo
        self.dataabertura = datetime.date.today()
        self.extrato = Extrato()

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO:", valor, "Data:", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True

    def transfereValor(self, contadestino, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente"
        else:
            contadestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            return "Transferencia Realizada"

    def gerarsaldo(self):
        print(f"numero: {self.numero}\nsaldo:{self.saldo}")
