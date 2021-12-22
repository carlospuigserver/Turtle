import turtle
turtle.Turtle()
l=100
a=45
turtle.speed(0)
turtle.bgcolor("yellow")
turtle.color("purple")
turtle.width(20)
for _ in range(8):
    turtle.forward(l)
    turtle.left(a)
turtle.done()