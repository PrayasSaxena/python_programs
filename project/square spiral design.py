import turtle

col=('white','red','orange','yellow','green','cyan','blue')

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(0)

for i in range(100):
   t.forward(i*4)
   t.right(91)
   t.color(col[i%7])

for b in range(3):
    t.forward(i*4)
    t.right(91)

for c in range(2):
    t.forward(i*4)
    t.right(91)
