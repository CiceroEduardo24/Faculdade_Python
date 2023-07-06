from Encapsulamento02 import *

class Profissional(Pessoa):
    def __init__(self, nome, idade, Profissao):
        super().__init__(nome, idade)
        self.Profissao = Profissao
    def imprimir(self):
        super().imprimir()
        print(f"\t e trabalha com {self.Profissao}")

p= Profissional("Ana", 24,"balconista")
p.imprimir()
