# Programa que realice cualquiera de las figuras anteriores
print("Selecciona la figura que quieres crear,")
print("Puedes elegir entre las siguientes figuras:")
carlos=input("Triángulo,Cuadrado,Pentágono,Hexágono,Octógono y Decágono:   ")
import turtle
turtle.Turtle
l=100
turtle.bgcolor("blue")
turtle.color("pink")
turtle.width(10)
turtle.speed(0)
if carlos=="Triángulo":
    for _ in range(3):
        turtle.forward(l)
        turtle.left(120)
elif carlos=="Cuadrado":
    for _ in range (4):
        turtle.forward(l)
        turtle.left(90)
elif carlos=="Pentágono":
    for _ in range(5):
        turtle.forward(l)
        turtle.left(72)
elif carlos=="Hexágono":
    for _ in range (6):
        turtle.forward(l)
        turtle.left(60)
elif carlos=="Octógono":
    for _ in range (8):
        turtle.forward(l)
        turtle.left(45)
elif carlos=="Decágono":
    for _ in range (10):
        turtle.forward(l)
        turtle.left(36)
else:
    print("Has escrito mal el nombre del polígono, o no esta entre las opciones a seleccionar")
turtle.done()

