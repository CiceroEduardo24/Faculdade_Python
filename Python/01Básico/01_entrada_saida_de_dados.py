#primeiro exercicio
a=['10']
b=['20']
c=['30']
r=a+b+c
t=a*2+b*3+c*4
print(r)
print(t)
#segundo execicio
#  f(x)=ax+b
# x=-b/a e diferente de 0
a=10
b=5
x=-b/a
print(f'Raiz da equação={x}')

#Entrada de dados
a = input('Digite algo')
#saída de dados
print(a)
"""Eval() = trata uma string como um valor numérico"""
numero = eval(input('digite uma inteiro:'))
numero += 2
print(f'Resultado = {numero}')

#FORMATAÇÃO DE DADOS DE SAÍDA
a=10
b=20
c=30
print('{}:{}:{}'.format(a,b,c))
#ou
print(f'{a}:{b}:{c}')
#Largura do campo a ser exibido
print(f'{a:5}:{b:4}:{c:3}')

"""Oito espaço e apenas 5 serão ultilizados"""
d=4.5555
f=6.999999
print('---------------------')
print(d)
print(f)
print(f'{d:5.3}:{f:4.3}')

#Imprimir uma sub string
str='Hello word!'
print(str[2:4])
#Imprimir uma sub string da direita pra esquerda
print(str[::-1])
print(str[4:2:-1])
