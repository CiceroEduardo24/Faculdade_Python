"""
Implementar uma solução em python, através do uso de thereads, qu efaça:
a. Inicie a execução de uma Thread
b.Coloque a thread para esperar 2 segundos
c.Informe o inicio  e o fim da execução da Thread
"""
from time import sleep
from threading import Thread
def tarefa(tempo_espera, mensagem):
    print(f'\nIniciando a Thread{mensagem}')
    sleep(tempo_espera)
    print(f'Concluindo a Thread')

thread = Thread(target=tarefa,args=(10,'\nThreads em execução',))
thread.start()
print('\n Aguardando pela execução da thread...')
thread.join()
print("A execução foi concluida!")