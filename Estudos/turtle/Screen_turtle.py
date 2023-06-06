import turtle

s = turtle.Screen()
t = turtle.Turtle(shape='turtle')
t.penup()
t.goto(-300, 0)
t.pendown()

t.pensize(3)
x= -100
y= 100
t.undo()
t.penup()
t.goto(x, y)
t.pendown()
t.circle(100)
t.penup()
soma=0
x = -500
y = 0
while soma<=10:
    soma +=1
    x +=100
    t.pensize(3)
    t.undo()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(100,90)
    t.left(90)

    t.penup()
