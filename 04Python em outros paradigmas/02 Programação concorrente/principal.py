from threading import Thread
from multiprocessing import Process
"""
Processo:
O processo é uma instância de um programa em execução. Ele é composto pelo código que está sendo executado,
os dados utilizados pelo programa (exemplo: valores de variável) e o estado ou contexto do processo.

Threads:
A thread pertence a um determinado processo. Múltiplas threads podem ser executadas dentro de um mesmo processo. 
As de um mesmo processo compartilham a área de memória e podem acessar os mesmos dados de forma transparente.

Atenção!
Normalmente, utilizamos thread para interface gráfica, acesso ao banco de dados, acesso à rede etc.
Pois o programa não pode parar, ou a interface congelar, enquanto esperamos baixar um arquivo, por exemplo.
A thread é mais rapida que o processo;
"""
def funcao_a(nome):
    print(nome)

if __name__ == '__main__':
    t = Thread(target=funcao_a, args=("Minha Thread",))
    t.start()
    p = Process(target=funcao_a, args=("Meu Processo",))
    p.start()