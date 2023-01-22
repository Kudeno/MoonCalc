import ephem
import datetime
now = datetime.datetime.now()
moon = ephem.Moon()
moon.compute(now)
next_full_moon = ephem.next_full_moon(now.strftime("%Y/%m/%d"))
print("Ecco quando la luna sarà nuovamente piena: ", next_full_moon)