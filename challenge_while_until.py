#challenge turle until condition
import turtle
pencilColor = input("Enter pencil color :")
lineLength = int(input("Enter line lenght: "))
noOfLines = int(input("Enter no of lines you need"))
angle = int(input("Enter angle : "))
while noOfLines != 0:
    turtle.forward(lineLength)
    turtle.color(pencilColor)
    turtle.right(angle)
    noOfLines = noOfLines - 1
    
    
