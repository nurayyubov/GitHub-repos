# Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya yozing
import datetime as dt

hozir = dt.datetime.now()
bugun = hozir.date()
tugilganim = dt.date(2004, 3, 5)

yillar = bugun.year - tugilganim.year
oylar = bugun.month - tugilganim.month
kunlar = bugun.day - tugilganim.day

if kunlar < 0:
    oylar -=1
    kunlar +=30
    
if oylar <0:
    yillar -=1
    oylar+= 12
    
print(f"Tug'ilganimdan beri {yillar} yil, {oylar} oy, {kunlar} kun bo'ldi")
