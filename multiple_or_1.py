##multiple or
import datetime
date=input("Enter the date(mm/dd/yyyy): ")
date=datetime.datetime.strptime(date,"%m/%d/%Y").date()
if date.strftime("%B")=="April" or date.strftime("%B")=="June" or \
   date.strftime("%B")=="September" or date.strftime("%B")=="November":
    print("Month has 30 days")
   
