from contaCliente import ContaCliente
class ContaComum(ContaCliente):
    def __init__(self, numero, IOF, IR, valorInvestido,taxaRendimento):
        super().__init__(numero, IOF, IR, valorInvestido, taxaRendimento)

    def CalculoRendimento(self):#(2)
        self.valorInvestido += (self.valorInvestido * self.taxaRendimento)