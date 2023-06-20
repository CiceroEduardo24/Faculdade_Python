#Multabilidade
def sum(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(sum([2,4,6,8,10]))

#segundo exemplo
lista = ['ferrari']
nova_lista = lista + ['porche']
print(nova_lista)

#terceiro exemplo
import operator
print(operator.add(10,20))

#quarto exemplo
from functools import reduce
print(reduce(operator.add(10,20)))
print(reduce(operator.concat,['Aprendendo reduce...']))