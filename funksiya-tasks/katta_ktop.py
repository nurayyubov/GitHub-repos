# Foydalanuvchidan ikkita son olib,
# ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

def katta_ktop(a, b):
    if a>b:
        print(f"{a} soni {b} sonidan katta")
    elif a<b:
        print(f"{b} soni {a} sonidan katta")
    else:
        print(F"{a} va {b} sonlari teng")
        
katta_ktop(-12, 0)

    
    