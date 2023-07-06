""""em Python todos os blocos são iniciados com o símbolo :
 (dois pontos) na linha superior e representados pelo acréscimo
  de 4 (quatro) espaços à esquerda. Sem se preocupar por enquanto com o significado
  das expressões for, if, else ou range, observe os códigos abaixo:
"""
a = 0
for i in range(30):
    if a % 2 == 0:
        a += 1
        continue
    else:
        if a % 5 == 0:
            break
        else:
            a += 3
print (a)