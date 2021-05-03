#timedelta function
import datetime
current_date=datetime.date.today()
expire_date=current_date+datetime.timedelta(days=15)
print("your expairation date is " + expire_date.strftime("%d/%B"))
