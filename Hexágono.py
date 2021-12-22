# Angulo hexagono= 360/6
import turtle
turtle.Turtle()
longitud=100
angulo=60
turtle.speed(0)
turtle.bgcolor("blue") # Color fondo
turtle.color("red") # Color lineas
turtle.width(20) # Ancho lineas

for _ in range(6):
    turtle.forward(longitud)
    turtle.left(angulo)
turtle.done()    