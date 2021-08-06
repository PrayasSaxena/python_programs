import turtle

col=('red','yellow','green','cyan','blue','white')
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(10)
c=0

for i in range(50):
   t.color(col[c])
   t.forward(i*10)
   t.right(144)
   if c==3:
       c=0
   else:
       c+=1    
