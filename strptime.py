import datetime
birthday=input("What is your birthday?(dd-mm-yyyy)")
birthdate=datetime.datetime.strptime(birthday,"%d-%m-%Y").date()
print(birthdate)
print("your birth month is " + birthdate.strftime("%B"))
print("your birth day is " + birthdate.strftime("%A"))
