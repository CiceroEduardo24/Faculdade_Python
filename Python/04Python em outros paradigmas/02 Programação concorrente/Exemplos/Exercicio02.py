"""
Implementar uma solução em python com o uso de Threads, que faça;
a.Inicie a execução de 2 threads
b.A primeira threads deve calcular o cubo de um numero
c.A segunda Thread deve calcular o quadrado de um numero
d.Coloque a primeira  e a segunda thread para esperar, respectivamente 3 e 2 segundos
e.Informe a ordem de execução das thrreads
"""
import math
from time import sleep
from threading import Thread
from math import pow
def cubo(numero, tempo):
    a = math.pow(numero,3)
    sleep(tempo)
    print(f"o cubo de {numero} e: {int(a)}")

def quadrado(numero, tempo):
    a = math.pow(numero,2)
    sleep(tempo)
    print(f"o quadrado de {numero} e: {int(a)}")

t1 = Thread(target=cubo,args=(5,3))
t2 = Thread(target=quadrado,args=(5,2))
t1.start()
t2.start()
t1.join()
t2.join()
print("Fim da execução!")