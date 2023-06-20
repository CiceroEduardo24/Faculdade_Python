from At01 import Veiculo

class Onibus(Veiculo):
    def capacidade(self,capacidade=70):
        return super().capacidade(capacidade=70)

onibus_escolar = Onibus("Scania",200,50)
onibus_escolar.toStr()
onibus_escolar.capacidade()