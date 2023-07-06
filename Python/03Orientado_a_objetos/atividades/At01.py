class Veiculo:
    def __init__(self,nome, velocidadeMax, quilometroPorLitro):
        self.nome = nome
        self.velocidadeMax = velocidadeMax
        self.KmPorL = quilometroPorLitro

    def capacidade(self,capacidade):
        print(f"Capacidade máxima permitida:{capacidade}")

    def toStr(self):
        print(f'nome = {self.nome}')
        print(f'valociade máxima = {self.velocidadeMax}')
        print(f'Km por litro = {self.KmPorL}')
