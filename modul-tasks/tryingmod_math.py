# math modulini import qiling va quyidagi masalalarni yeching:
# 1. 64 ning kvadrat ildizini hisoblang.
# 2. Sin(45 daraja) va Cos(45 daraja) ni hisoblang.
# 3. Pi yordamida doira yuzini hisoblash uchun funksiya yozing (radiusni argument sifatida oling).

import math
#1
x=64
print(math.sqrt(x))
#2
a=45
rad=math.radians(a)
print(math.asin(rad))
print(math.acos(rad))
#3
def doirayuzi(radius):
    r = float(radius)
    s = (math.pi)*(r**2)
    return s
print(doirayuzi(3))

    
    
    

