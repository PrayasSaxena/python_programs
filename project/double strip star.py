import turtle

col=('red','yellow','green','cyan','blue','white')

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(30)

for i in range(100):
   t.pencolor(col[i%6])
   t.forward(i*4)
   t.left(150)
   t.width(2)
