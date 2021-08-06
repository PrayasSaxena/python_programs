import turtle

col=('red','yellow','green','cyan','blue','white')

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(25)

for i in range(150):
   t.color(col[i%6])
   t.forward(i*1.5)
   t.left(59)
   t.width(3)
