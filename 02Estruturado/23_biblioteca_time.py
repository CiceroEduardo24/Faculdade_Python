import time
while True:
    x = time.time()
    print(f'Local time: {time.ctime(x)}')
"""
Função	               Retorno
time()	               Número de segundos passados desde o início da contagem (epoch). Por padrão, 
                       o início é 00:00:00 do dia 1 de janeiro de 1970.
ctime(segundos)	       Uma string representando o horário local, calculado a partir do número de 
                       segundos passado como parâmetro.
gmtime(segundos)	   Converte o número de segundos em um objeto struct_time descrito a seguir.
localtime(segundos)	   Semelhante à gmtime(), mas converte para o horário local.
sleep(segundos)	       A função suspende a execução por determinado número de segundos.
"""