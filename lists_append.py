#adding elements to the list
guests = []
print("enter 0 if there are no guests to add")
name = ""

while name != "0":
    name = input("Enter the name of the guest ")
    guests.append(name)
for value in range(len(guests)-1):
    print(guests[value])
