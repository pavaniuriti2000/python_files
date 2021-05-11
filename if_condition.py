#if_else condition
answer=input("Would you like express shipping?")
if answer=="yes":
    print("That will be an extra 10$")
    acceptance=input("Do you wnat to continue: ")
    if acceptance=="yes":
        print("your toatal cost is 110$")
    else:
        print("We have not added any shipping cost")
else:
    print("We have not added any shipping cost")
