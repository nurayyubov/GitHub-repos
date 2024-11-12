# Foydalanuvchidan son qabul qilib, 
# sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya
def bolinuvchitop(son):
    for n in range(2, 11):
        if not son%n:
            print(f"{son} soni {n} soniga qoldiqsiz bo'linadi.")

bolinuvchitop(34)
