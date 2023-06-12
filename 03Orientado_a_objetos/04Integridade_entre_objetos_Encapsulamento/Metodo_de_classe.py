"""
Os métodos de classe são a maneira indicada para se acessar os atributos de classe.
Eles têm acesso diretamente à área de memória que contém os atributos de classe.
"""
class Circulo:
    _total_circulos = 0

    def __init__(self,pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        type(self)._total_circulos +=1

    @classmethod
    def gettotal_circulos(cls):
        return cls._total_circulos