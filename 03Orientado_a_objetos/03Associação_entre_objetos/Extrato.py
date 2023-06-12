# composição
class Extrato:
    def __init__(self):
        self.transacoes = []

    def extrato(self, numeroconta):
        print(f"Extrato: {numeroconta} \n")
        for p in self.transacoes:
         print(f"{p[0]}{p[1]:10.2f}  {p[2]:6s}{p[3].strftime('%d/%m/%y %H:%M:%S')}")