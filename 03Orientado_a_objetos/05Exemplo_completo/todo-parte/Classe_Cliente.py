#Agregação parte 2
from Class_Conta import Conta
class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

c1 = Cliente("111111111-11", "ana",
             "Rua das Maringueiras")
c2 = Cliente("222222222-22", "Cicero",
              "Rua das Graças")
conta = Conta([c1,c2],24237196,2500.00)
conta.depositar(1000)
conta.sacar(500)
conta.extrato.imprimir()