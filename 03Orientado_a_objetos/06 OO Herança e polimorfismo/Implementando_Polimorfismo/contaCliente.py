import datetime
class ContaPoupanca:
    def __init__(self, taxaremuneracao):
        self.taxaremuneracao = taxaremuneracao
        self.data_abertura = datetime.datetime.today()

    def remuneracaoConta(self):
        self.saldo += self.saldo * self.taxaremuneracao

class ContaCliente:
    def __init__(self, numero, IOF, IR, valorInvestido, taxaRendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorInvestido = valorInvestido
        self.taxaRendimento = taxaRendimento

    def CalculoRendimento(self):
        self.valorInvestido +=(self.valorInvestido * self.taxaRendimento)
        self.valorInvestido = (self.valorInvestido - (self.taxaRendimento * self.IOF * self.IR))

    def Extrato(self):#(1)
        print(f'O saldo atual da conta {self.numero} é {self.valorInvestido:10,2f}')