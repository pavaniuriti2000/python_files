#solving quadratic equation
import cmath
print("quadratic equation form is ax^2+bx+c enter a,b,c vaues along with one x value")
a=int(input("Enter a value x^2 quoficient:"))
b=int(input("Enter b value x coeficient: "))
c=int(input("Enter c value constant: "))
#x=int(input("Enter constant x value: "))
#discriminant  d
d=(b**2)-(4*a*c)
#solution 1
sol1=(-b-cmath.sqrt(d))/(2*a)
#solution 2
sol2=(-b+cmath.sqrt(d))/(2*a)
print("solution 1 is: "+str(sol1))
print("solution 2 is :"+str(sol2))
