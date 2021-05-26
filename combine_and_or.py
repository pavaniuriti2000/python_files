#combine and , or ina single if statement
country = input("Enter your country name:")
pet=input("Enter your pet :")
country=country.lower()
pet=pet.lower()
if country == "canada" and \
   pet == "beaver" or \
   pet == "moose":
    print("Do you play hockey too")
