from abc import ABC
class ContaCliente(ABC):
    def __init__(self, numero,IOF,IR, valorInvestimento, valorRendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorInvestimento = valorInvestimento
        self.valorRendimento = valorRendimento

    @abstractmethod
    def CalculoRendimento(self):
        pass