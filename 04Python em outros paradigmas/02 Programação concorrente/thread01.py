import threading
import time
# Exemplo de funcao sem parametros
def funcao():
     for i in range(3):
         print(i,"execultando a thread")
         time.sleep(1)
print('Iniciando o programa')
threading.Thread(target=funcao()).start()
print('Finalizando o programa')