# Tipos de associação entre objetos
"""
conta1 = Conta(1, 123, 'Joao',0)
conta2 = Conta(3, 456, 'Maria',0)
conta1.depositar(1000)
print(conta1.saldo)
print(conta2.saldo)
print(conta1.saldo)


cliente1 = Cliente(123, "Joao", "Rua 1")
cliente2 = Cliente(345, "Maria","Rua 2")
conta1 = Conta([cliente1,cliente2], 1,0)
conta1.gerarsaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()
"""
from Cliente import Cliente
from Conta import Conta

cliente1 = Cliente('123', 'Joao', 'Rua X')
cliente2 = Cliente('456', 'Maria', 'Rua W')
conta1 = Conta([cliente1], 1, 2000)
conta2 = Conta([cliente2], 2, 6000)
conta2.depositar(1000)
conta2.extrato.extrato(conta2.numero)
conta2.gerarsaldo()