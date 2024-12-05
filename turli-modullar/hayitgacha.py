# Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring
import datetime as dt
hozir = dt.datetime.now()
bugun = hozir.date()
rhayit = dt.date(2025, 3, 30)
rfarq = rhayit - bugun
qhayit = dt.date(2025, 6, 6)
qfarq = qhayit - bugun
print(f"Ramazon hayitigacha {rfarq.days} kun qoldi")
print(f"Qurbon hayitigacha {qfarq.days} kun qoldi")


