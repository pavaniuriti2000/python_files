#-----------reading input from user and using loop variable--------
import turtle
num_of_sides=int(input("Enter number of sides : "))
for steps in range(num_of_sides):
    turtle.forward(100)
    turtle.right(360/num_of_sides)
    for moresteps in range(num_of_sides):
        turtle.forward(50)
        turtle.right(360/num_of_sides)
        
    
