#challenge in making_complex_decisions
tax = 0
total = 0
country = input("Enter what country you are from :")
country = country.lower()
total = float(input("Enter total "))
if country == "canada":
    province = input("Enter your province ")
    
    province = province.lower()
    if province == "alberta":
        tax = (0.05 * total) 
    elif province == "ontaria" or province == "nova scotia":
        tax = (0.13 * total)
    else:
        tax = (0.05 * total) + (0.06 * total)

else :
    tax = 0

total = total +tax
print("Your tax amount is $%.2f" %tax)
print("Your total amount is $%.2f" %total)
