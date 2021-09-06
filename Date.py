import datetime
x=datetime.datetime.now()
print(x)

#print the year and weekday
import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# datetime constructor
import datetime
x=datetime.datetime(2021,8,9)
print(x)

#strftime() function print the date objcts as readable strings
import datetime
x=datetime.datetime(2021,8,9)
print(x.strftime("%B"))