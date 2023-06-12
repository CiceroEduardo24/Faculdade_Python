# Métodos da classe
class NomeCompleto:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    @classmethod
    def fromString(cls,texto): # Padrão Factory
        nome, sobrenome = map(str, texto.split(' '))
        objeto = cls(nome, sobrenome)
        return objeto
    #Mesmo exemplo com método estático
    @staticmethod
    def isValid(texto):
        nomes = texto.split(' ')
        return len(nomes)>1

registro1 = NomeCompleto.fromString("Cicero Eduardo")
