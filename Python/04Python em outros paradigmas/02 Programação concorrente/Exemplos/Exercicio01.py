"""
Implementar uma solução em python, com o uso de Threads, que faça:
 a.Inicie a execução de duas Threads
 b.Coloque a primeira e a segunda thread para esperar, respecyivamente, 3 e 2 segundos
 c.Informe a ordem da execução da threads
"""
from time import sleep
from threading import Thread
def tarefas(tempo, mensagem):
    print(f'iniciando a tarefa{mensagem}')
    sleep(tempo)
    print(f'Conclusão da tarefa{mensagem}')

t1 = Thread(target=tarefas, args=(3, " A"))
t2 = Thread(target=tarefas, args=(2, " B"))
t1.start()
t2.start()
t1.join()#esperar até completar a execução thread 1
t2.join()#esperar até completar a execução thread 2
print("Execução concluída!")