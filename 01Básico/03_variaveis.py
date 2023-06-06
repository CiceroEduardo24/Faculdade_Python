"""Não se declara os tipos das variaveis"""
Nome = "Arthur"
print(Nome)

"""
OPERADOR	NOME
+=	         mais igual
-=	         menos igual
*=	         vezes igual
/=	         dividido igual
%=	         módulo igual
"""
#Atribuições multiplas
a, b = 1, 2
print('Antes da troca')
print(f"O valor das variaveis: a={a}, b={b}")
# Primeira troca
temp = a
a = b
b = temp
print('Primeira troca')
print(f"O valor das variaveis: a={a}, b={b}")
# Segunda troca
a, b = b, a
print('Segunda troca')
print(f"O valor da variaveis são: a={a}, b={b}")

"""Variáveis Locais e Globais"""
def multiplicador(numero):
    a = 2  # esta variável tem escopo local
    print(f"Dentro da função, a variável vale: {a}")
    return a * numero


a = 3  # esta variável tem escopo global
b = multiplicador(5)
print(f"Fora da função, a variável a vale: {a}")

#Relação de precedência entre operadores

"""
Operador	                            Descrição

[expressões ...]	                    Definição de lista
x[ ], x[índice : índice]	            Operador de indexação
**	                                    Exponenciação
+x, -x	                                Sinal de positivo e negativo
*, /, //, %	                            Produto, divisão, divisão inteira, resto
+, -	                                Soma, subtração
in, not in, <, <=,>, >=, <>, !=, ==	    Comparações, inclusive a ocorrência em listas
not x	                                Booleano NOT (não)
and	                                    Booleano AND (e)
or	                                    Booleano OR (ou)
"""

#Conversões de tipos de dados
