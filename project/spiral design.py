import turtle

col=('red','pink','orange','yellow','green','blue')

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(0)

for i in range(300):
   t.color(col[i%6])
   t.forward(i)
   t.left(20)
   t.width(i/5+1)
