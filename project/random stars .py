import turtle
import random

t=turtle.Turtle()

for a in range(1,11):
    t.penup()
    t.setx(random.randint(-300,300))
    t.sety(random.randint(-300,300))
    t.pendown()
    for c in ['red','yellow','green','blue','black']:
        t.color(c)
        t.forward(50)
        t.left(144)




 
     