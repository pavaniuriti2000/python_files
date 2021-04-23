#challenge on for loop,turlte,nested loop,read from user
import turtle
numOfSides=int(input("Enter number of sides: "))
for steps in range(numOfSides):
    turtle.forward(100)
    turtle.right(360/numOfSides)
    for moresteps in range(numOfSides):
        turtle.forward(50)
        turtle.right(360/numOfSides)
