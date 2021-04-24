#calculate the days until my next birthday
import datetime
birthDay=input("Enter your next birthday date(dd/mm/yyyy): ")
birthDate=datetime.datetime.strptime(birthDay,"%d/%m/%Y").date()
currentDate=datetime.date.today()
print("number of days left "+str(birthDate-currentDate))
