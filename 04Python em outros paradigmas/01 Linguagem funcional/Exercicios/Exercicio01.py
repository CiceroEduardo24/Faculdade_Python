lista = [0,1,2,3,4,5,6,7,8,9]
fResult = lambda x: x % 2 == 0
pares = list(filter(fResult, lista))
print(pares)