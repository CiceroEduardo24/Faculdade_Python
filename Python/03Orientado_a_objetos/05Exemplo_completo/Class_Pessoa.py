# Atributos estáticos
class Pessoa:
    _contador = 0 # Atributo estático
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa._contador += 1
    def imprimir(self):
        print(self.nome,"tem",
              self.idade,"anos")
    @property # Propriedade
    def contador(self):
        return type(self._contador)

p1 = Pessoa("Carlos",18)
p1 = Pessoa("Carlos",18)
p1 = Pessoa("Carlos",18)
p1 = Pessoa("Carlos",18)
print(p1.contador)
print(Pessoa._contador)