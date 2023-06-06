import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.forward(100)
t.left(90)
u = turtle.Turtle()
u.left(90)
u.forward(100)
t.forward(100)
u.right(45)
#Metodos turtle
"""
Uso Explicação
t.forward(distância)             Mova a tartaruga na direção em que ela está apontando
                                 por distância pixels
t.left(ângulo)                   Gire a tartaruga em sentido anti-horário por ângulo graus
t.right(ângulo)                  Gire a tartaruga em sentido horário por ângulo graus
t.undo()                         Desfaça o movimento anterior
t.goto(x, y)                     Mova a tartaruga para as coordenadas definidas por x e y; se a
                                 caneta estiver abaixada, desenhe uma linha
t.setx(x)                        Defina a primeira coordenada da tartaruga como x
t.sety(y)                        Defina a segunda coordenada da tartaruga como y
t.setheading(ângulo)             Defina a orientação da tartaruga como ângulo, dado em graus;
                                 o ângulo 0 significa leste, 90 significa norte e assim por diante
t.circle(raio)                   Desenhe um círculo com o raio indicado; o centro do círculo
                                 está a raio pixels à esquerda da tartaruga
t.circle(raio,ângulo)            Desenhe apenas a parte do círculo (ver acima) correspondente ao ângulo
t.dot(diâmetro, cor)             Desenhe um ponto com o diâmetro e cor indicados
t.penup()                        Levante a caneta; não desenha ao movimentar
t.pendown()                      Desça a caneta; desenha ao movimentar
t.pensize(largura)               Desfina a espessura da linha da caneta como largura
t.pencolor(cor)                  Defina a cor da caneta como aquela descrita pela string cor
"""

#Screen
"""
Uso                Explicação
s.bgcolor(cor)     Muda a cor do fundo da tela s para a cor descrita por meio da string cor
s.clearscreen()    Apaga a tela s
s.turtles()        Retorna a lista de todas as tartarugas na tela s
s.bye()            Fecha a janela da tela s
"""