from threading import Thread, Lock
from multiprocessing import Process
import time

"""
Cada thread é executada em um determinado tempo t. Em t1, a thread1 lê e incrementa o contador,
que passa a valer 1. Em t2, a thread2 lê o contador (valor 1). Em t3, a thread3 lê e incrementa 
o contador, que passa a valer 2. Em t4, a thread2 incrementa o contador, porém a partir do valor 
que ela leu, que era 1.

No final, o contador passa a valer 2, erroneamente. Esse resultado inesperado devido à sincronia 
na concorrência de threads (ou processos) se chama condição de corrida.

Para evitar a condição de corrida, utilizamos a primitiva lock (trava). Um objeto desse tipo tem 
somente dois estados: travado e destravado. Quando criado, ele fica no estado destravado. Esse 
objeto tem dois métodos: acquire e release
"""
contador = 0

def funcao_a(indice):
    global contador
    for i in range(1000000):
        contador += 1
    print("Termino thread ", indice)

if __name__ == '__main__':
    tarefas = []
    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino!", contador)

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", contador)