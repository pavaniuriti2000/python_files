#time formats
import datetime
current_time=datetime.datetime.now()
print("current time is" +datetime.datetime.strftime(current_time,"%H:%m:%S"))
print("current time is" +datetime.datetime.strftime(current_time,"%I:%m %p"))

