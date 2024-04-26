import turtle

x = turtle.Turtle()
x.speed(100)

def figura(l,c):
  for i in range(10):
    x.forward(l)
    x.left(360/c)
    
#casa    
figura (100,4)
#porta
x.penup()
x.forward(35)
x.goto(65,30)
x.pendown()
figura (30,4)
#qrFinestra
x.penup()
x.goto(15,60)
x.pendown()
figura(20,4)
#2nfinestra
x.penup()
x.goto(85,80)
x.pendown()
figura(20,4)
#tejado
x.penup()
x.goto(0,100)
x.pendown()
figura(100,3)
#suelo
x.penup()
x.goto(0,0)
x.right(120)
x.pendown()
x.forward(200)
x.backward(400)
