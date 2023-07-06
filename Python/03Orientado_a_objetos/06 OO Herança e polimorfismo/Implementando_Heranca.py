from ContasClientesExtrato import conta
import datatime
class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if(self.saldo + self.limite) < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor "DATA", datetime.datetime.today()])
            return True
        """
        A execução no terminal gera o seguinte:

>>>from clientes import Cliente
... from ContasClientesExtrato import Conta
... from ContaEspecial import ContaEspecial
... cliente1 = Cliente("123","Joao","Rua X")
... cliente2 = Cliente ("456","Maria","Rua W")
... cliente3 = Cliente ("789","Joana", "Rua H")
... conta1 = Conta([cliente1,cliente2],1,2000)
... conta2 = ContaEspecial([cliente3],3,1000,2000)
... conta2.depositar(100)
... conta2.sacar(3200)
Valor do saque 3200.00 maior que o valor do saldo mais o limite 3100.00
>>> conta2.extrato.extrato(conta2.numero)
Extrato : 3
DEPÓSITO 100.00 Data 14/Jun/2020
        """