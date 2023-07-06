"""
   Para tornar um atributo privado, é preciso iniciá-lo com dois underscores (‘__’).
   E qual seria o retorno do interpretador ao se acessar um atributo privado para
   classe Conta? Um erro seria gerado.
"""


class Conta:
    def __init__(self, numero):
        self.numero = numero
        self._saldo = 0

    """
    Decorator @property
    
    Uma estratégia importante disponibilizada pelo Python são as properties. 
    Utilizando o decorator property nos métodos, mantém-se os atributos como 
    protegidos, os quais, por sua vez, são acessados apenas por meio dos métodos 
    “decorados” com property
    """
    @property
    def saldo(self):
        return self._saldo
    """
    Os métodos decorados com a property @setter forçam todas alterações de valor 
    dos atributos privados a passar por esses métodos.
    Notação:
    @< nomedometodo >.setter
    """
    @saldo.setter
    def saldo(self, saldo):
        if (self.saldo < 0):
            print("saldo inválido")
        else:
            self._saldo = saldo
    #_________________Os properties ajudam a garantir o encapsulamento no Python.___________________

def main():
   #conta = Conta(1, 1000)
   #saldo = conta.__saldo
   #saldo = conta._Conta__saldo
    """como acessar os método decorados
    com @property e @ < nomedometodo >.setter"""
    conta = Conta(1)
    conta.saldo = 100  # usando o @saldo.setter
    print(f'saldo da conta = {conta.saldo}')  # usando o @property
   #print(saldo)



if __name__ == "__main__":
    main()