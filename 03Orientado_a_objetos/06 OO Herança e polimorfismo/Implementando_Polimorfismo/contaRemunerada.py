from contaCliente import ContaCliente
class ContaRemunerada(ContaCliente):
    def __init__(self,numero,IOF,IR,valorInvestido,taxaRendimento):
        super().__init__(numero, IOF, IR, valorInvestido, taxaRendimento)

    def CalculoRendimento(self):#(3)
        self.valorInvestido += (self.valorInvestido * self.taxaRendimento)
        self.valorInvestido -= self.valorInvestido * self.IOF