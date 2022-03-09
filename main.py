import turtle as t
import random as r
lista_boja = [(26, 108, 164), (193, 38, 81), (237, 161, 50)]
tim = t.Turtle()
t.colormode(255)


screen = t.Screen()
tim.pensize(20)
tim.shape("circle")
for i in range(-360,360,50):
    tim.penup()
    for j in range(360,-360, -50):
        tim.goto(j,i)
        tim.color(lista_boja[r.randint(0, len(lista_boja) - 1)])
        tim.stamp()


















screen.exitonclick()

