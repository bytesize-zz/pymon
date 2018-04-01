import time
import datetime



dt = datetime.datetime.now()
dtutc = datetime.datetime.utcnow()
td = dt - dtutc

print(dt)
print(dtutc)
print(td)

dt = dt.strftime("%A %d.%m.%y %H:%M")
dt2 = dtutc.strftime("%A %d.%m.%y %H:%M")

s = td.seconds
days = s // 86400
s = s - (days*86400)
hours = s // 3600
s = s - (hours*3600)
minutes = s // 60
seconds = s - (minutes*60)

print("%sd %sh %sm %ss" %(days, hours, minutes, seconds))
print(td)
print(dt)