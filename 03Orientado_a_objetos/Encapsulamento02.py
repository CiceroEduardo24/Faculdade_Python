# Encapsulamento
class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)

    def imprimir(self):
        print(f'nome:{self.get_nome()}, Endereço:{self.get_ender()}')

    def set_nome(self, nome): #getters
        self.nome = nome

    def set_ender(self, ender):#setters
        self.ender = ender

    def get_nome(self):
        return self.nome

    def get_ender(self):
        return self.ender


# Objeto pessoa
pessoa1 = Pessoa("maria", "rua 01234")
pessoa1.imprimir()
