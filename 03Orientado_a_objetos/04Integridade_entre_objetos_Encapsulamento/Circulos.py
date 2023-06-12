from Atributos_de_Classe import Circulo
"""
circ1 = Circulo(1,1,10)
circ1.total_Circulos
circ2 = Circulo(2,2,20)
circ2.total_Circulos
Circulo.total_Circulos

Esse acesso direto ao valor da variável de classe não é desejado. 
Deve-se colocar a variável com atributo privado com o underscore ‘_’.
"""
circ1 = Circulo(1,1,10)
circ1._total_Circulos
Circulo.total_Circulos