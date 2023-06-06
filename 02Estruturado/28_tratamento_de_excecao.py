try:
    num = eval(input("Entre com um número inteiro: \n"))
    print(num)
except ValueError:
    print("Mensagem 1")
except IndexError:
    print("Mensagem 2")
except:
    print("Mensagem 3")



"""
Exceção	              Explicação

KeyboardInterrupt	  Levantado quando o usuário pressiona CTRL+C, a combinação de interrupção.
OverflowError	      Levantado quando uma expressão de ponto flutuante é avaliada como um valor muito grande.
ZeroDivisionError	  Levantado quando se tenta dividir por 0.
IOError	              Levantado quando uma operação de entrada/saída falha por um motivo relacionado a isso.
IndexError	          Levantado quando um índice sequencial está fora do intervalo de índices válidos.
NameError	          Levantado quando se tenta avaliar um identificador (nome) não atribuído.
TypeError	          Levantado quando uma operação da função é aplicada a um objeto do tipo errado.
ValueError	          Levantado quando a operação ou função tem um argumento com o tipo correto, mas valor incorreto.
"""