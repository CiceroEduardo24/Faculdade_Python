#Composição
class Extrato:
    def __init__(self):
        self.transacoes = []
    def imprimir(self):
        for p in self.transacoes:
            print(p[0], p[1])
