# Mashq 1
# Berilgan roʻyxatdan (list) faqat bosh harfi A harfi bilan boshlanadigan elementlarni ajratib olish kerak. 
#Keyin bu elementlarning uzunligini (len) hisoblash kerak.
# Koʻrsatma:

# filter va startswith funksiyalaridan foydalaning.
# Soʻngra har bir element uzunligini hisoblash uchun map va lambda funksiyalaridan foydalaning.


royxat = ["Apple", "Banana", "Avocado", "Mango", "Apricot"]
aroyxat = list(filter(lambda x: x.startswith('A'), royxat))
uzunlik = list(map(len, aroyxat))
print(uzunlik)

