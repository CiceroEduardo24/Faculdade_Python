class Banco():
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adicinarConta(self, contaCliente):
        self.contas.append(contaCliente)

    def CalcularRendimentoMensal(self):#(7)
        for c in self.contas:
            c.CalculoRendimento()

    def imprimeSaldoContas(self):
        for c in self.contas:
            print()