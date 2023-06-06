"""numéricos"""
#----numeros inteiros----
a=1_000_000
print(type(a))

#-----tipos Float-----
b=50.0
print(type(b))
#soma
print(2+3+1)#int
print(2+3+1.0)#float
#exponenciação
print (2**3)
print (type(2**3))#int
print (type(2.0**3))#float
#divisão( // = quociente, % = resto)
x = 5/2
print(x)

#-----tipo complex---
r = complex(2,5)
r.conjugate()
print(r)
t=5+4j
print(type(t))

#-----Tipo bool---
print(2<3)
print(not(2<3))

#----Operadoes numéricos----
"""                           Exemplo
Operação 
matemática	Símbolo usado Equação	Resultado
Soma	       +	       2.5 + 1.3	3.8
Subtração	   -	       2.5 - 1.3	1.2
Multiplicação  *	       2.5 * 1.3	3.25
Divisão	       /	        2.5/1.3	    1.923076923076923
Divisão inteira	//	           9/2	    4
Resto na divisão
inteira	         %	             9%2	1
Valor absoluto abs(parâmetro) abs(-2.5)	2.5
Exponenciação	**	            2**4	16
"""
#----Operadores booleanos-------
"""

Símbolo usado	Descrição
<	            Menor que
<=	            Menor ou igual a
>	            Maior que
>=	            Maior ou igual a
==	            Igual
!=	            Não igual
"""

"""Tipos Sequenciais"""
#---Strings---
a = 'aBcD E'
print(str(a))
#todas as letras em maiusculas
b = a.upper()
print(b)
#todas as letras em minusculas
c = a.lower()
print(c)
#quebra a string em substrings
d = a.split()
print(d)

"""Lista sequencial"""

"""
[] = Usando um par de colchetes para denotar uma lista vazia.
[a], [a, b, c] = Usando colchetes, separando os itens por vírgulas.
[x for x in iterable] = Usando a compreensão de lista.
list() ou list(iterable) = Usando o construtor do tipo list.
"""
lista = [101,102,103,104,105]
print(f'lista[0] = {lista[0]}')
print(f'lista[1] = {lista[1]}')
print(f'lista[2] = {lista[2]}')
print(f'lista[3] = {lista[3]}')
print(f'lista[4] = {lista[4]}')
print(f'Lista completa ={lista}')

"""Tuplas"""
"""
() = Usando um par de parênteses para denotar uma tupla vazia.
a, b, c ou (a, b, c) = Separando os itens por vírgulas.
tuple() ou tuple(iterable) = Usando o construtor do tipo tuple.
"""
#range
"""O tipo range representa uma sequência imutável de números e frequentemente
 é usado em loops de um número específico de vezes, como o for.
 Ele pode ser chamado de maneira simples, apenas com um argumento
EX: range(3) cria  a sequência(0,1,2)
range(2, 7) cria a sequência (2, 3, 4, 5, 6).
range(2, 9, 3) cria a sequência (2,5,8)
 """

"""Operadores sequenciais comuns"""
"""
Uso	        Resultado
x in s	    True se x for um subconjunto de s
x not in s	False se x for um subconjunto de s
s + t	    Concatenação de s e t
n*s	        Concatenação de n cópias de s
s[i]	    Caractere de índice i em s
len(s)	    Comprimento de s
min(s)	    Menor item de s
max(s)	    Maior item de s
"""
#Dicionário
pessoas={1111:['nome 01'],2222:['nome 02'],3333:['nome 03'],4444:['nome 04']}
pessoas
print(f'primeira pessoa = {pessoas[1111]}')
print(f'quarta pessoa = {pessoas[4444]}')
