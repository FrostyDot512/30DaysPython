#1
from datetime import datetime
now = datetime.now()
print(now)                       
day = now.day                   
month = now.month              
year = now.year                 
hour = now.hour                 
minute = now.minute             
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute, timestamp)

#2
from datetime import datetime
nowAgain = datetime.now()
MyDate = nowAgain.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Current date is {MyDate}")

#3
from datetime import datetime
NowAGain = datetime.now()
Today = "5 December, 2019"
CurrentDate = NowAGain.strptime(Today, "%d %B, %Y")
print(CurrentDate)

#4
from datetime import datetime, date
currentToday = date(year=2026, month=3, day=7)
new_year = date(year=2027, month=1, day=1)
time_left = new_year - currentToday
print(time_left)

#5
from datetime import date, datetime
Backthen = date(year=1970, month=1, day=1)
Diff = currentToday - Backthen
print(Diff)


