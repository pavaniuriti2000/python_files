#challenge turle until condition
import turtle
pencilColor = input("Enter pencil color :")
lineLenght = int(input("Enter line lenght: "))
angle = int(input("Enter angle : "))
while lineLenght != 0:
    turtle.forward(lineLength)
    turtle.color(pencilColor)
    turtle.right(angle)
    lineLenght = int(input("Enter line lenght: "))
    
