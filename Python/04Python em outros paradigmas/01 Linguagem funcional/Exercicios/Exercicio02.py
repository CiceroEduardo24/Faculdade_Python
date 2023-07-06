lista_numeros = [9.56565, 7.98989, 3.07655, 6.76676]
lista_precisao = [2, 2, 3, 3]

arredondamento = lambda x,y: round(x,y)
resultado = list(map(arredondamento, lista_numeros, lista_precisao))

print(resultado)