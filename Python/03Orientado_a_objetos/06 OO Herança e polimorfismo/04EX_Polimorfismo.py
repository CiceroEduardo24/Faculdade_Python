class Veiculo:
    def rodar(self):
        print("Reduz o consumo do combustivel")

class VeiculoEletrico(Veiculo):
    def rodar(self):
        super().rodar()
        print("Esse veículo ultiliza eletricidade")

veiculo_eletrico = VeiculoEletrico()
veiculo_eletrico.rodar()