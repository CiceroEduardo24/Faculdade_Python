from Banco import *
from contaComum import *
from contaRemunerada import *

banco1 = Banco(999,"teste")
contacliente1 = ContaCliente (1,0.01,0.1,1000,0.05)
contacomum1 = ContaComum(2,0.01,0.1,2000,0.05)
contaremunerada1 = ContaRemunerada(3,0.01,0.1,2000,0.05)

banco1.adicinarConta(contacliente1) #(4)
banco1.adicinarConta(contacomum1) #(5)
banco1.adicinarConta(contaremunerada1) #(6)
banco1.CalcularRendimentoMensal() #(7)
banco1.imprimeSaldoContas() #(8)