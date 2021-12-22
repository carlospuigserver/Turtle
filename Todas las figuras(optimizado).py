# Programa que realice cualquiera de las figuras anteriores
print("Selecciona la figura que quieres crear,")
n=int(input("Para ello escribe el número de lados de tu figura:   "))
import turtle
turtle.Turtle
l=100
turtle.bgcolor("blue")
turtle.color("pink")
turtle.width(10)
turtle.speed(0)
for _ in range(n):
    turtle.forward(l)
    turtle.left(360/n)
turtle.done()