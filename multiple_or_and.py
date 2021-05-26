#combination of and ,or
country = input("Enter  fav country :")
pet = input("Enter pet :")
country = country.lower()
pet = pet.lower()
if country == "canada" and \
   pet == "moose" or \
   pet == "beaver":
    print("Do you paly hockey too")


