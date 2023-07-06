#Referências entre objetos na memória
from Conta import Conta
conta2 = Conta(3, 456,'Maria',0) #Objeto
conta1 = Conta(1, 123,'Joao',0)
conta1.depositar(1000)
conta1.transfereValor(conta2,500)
print(conta1.saldo)
print(conta2.saldo)
