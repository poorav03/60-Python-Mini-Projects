import time
from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time for the alarm: (24h HH:MM:SS)\n")
try:
    h,m,s=map(int,alarm_time.split(":"))
    assert 0<=h<=24 and 0<=m<=60 and 0<=s<60
except:
    print("Invalid time format.")
    exit(1)
print("Setting up alarm for %02d:%02d:%02d"%(h,m,s))

while True:
    now = datetime.now()
    if(now.hour,now.minute,now.second)==(h,m,s):
        print("Wake up!!!!!!!")
        playsound('C:/Users/DELL/Downloads/iphone_alarm.mp3')
        break
    time.sleep(1)


