"""
Existem algumas situações em que os sistemas precisam controlar valores associados
à classe, e não aos objetos (instâncias) das classes. É o caso, por exemplo, ao se
desenvolver um aplicativo de desenho, como o Paint, que precisa contar o número de
círculos criados na tela.
"""
class Circulo():
    _total_Circulos = 0
    def __init__(self,pontox,pontoy,raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        self._total_Circulos +=1