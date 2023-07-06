class ClassSomaMultiplica:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def somar(self):
        return self.a+self.b
    def multiplicar(self):
        return self.a*self.b

class Derivada(ClassSomaMultiplica):
    def subtrair(self):
        return self.a-self.b
    def dividir(self):
        return self.a/self.b

d = Derivada(10, 20)
print(f'A soma de 10 e 20 é:{d.somar()}')
print(issubclass(Derivada,ClassSomaMultiplica))