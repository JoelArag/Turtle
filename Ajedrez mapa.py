import turtle


joel=turtle.Turtle()
joel.speed(100)
joel.penup()
joel.goto(-200,-200)
joel.pendown()


midapantalla=400
x=int(input("quantes caselles de ample vols?"))
y=int(midapantalla/x)

def casella():
  for w in range(4):
    joel.forward(y)
    joel.left(90)
  joel.forward(y)
for i in range(x):
  for w in range(x):
    casella()
  joel.backward(400)
  joel.left(90)
  joel.forward(y)
  joel.right(90)
