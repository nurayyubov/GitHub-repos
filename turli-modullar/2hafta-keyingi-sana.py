#Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring

import datetime as dt
hozir = dt.datetime.now()
bugun = hozir.date()
sanalar= []
for a in range(10):
    keyingisana = bugun + dt.timedelta(weeks=2 * a)
    sanalar.append(keyingisana)
for sana in sanalar:
    print(sana)
    