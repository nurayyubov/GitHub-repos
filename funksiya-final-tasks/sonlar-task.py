# Mashq 2
# Sonlardan iborat roʻyxat berilgan. Siz roʻyxatdan faqat juft sonlarni ajratib olishingiz kerak va har bir juft sonning kvadratini hisoblab yangi roʻyxat yaratishingiz kerak.
# Koʻrsatma:

# Juft sonlarni ajratish uchun filter va lambda funksiyalaridan foydalaning.
# Kvadratini hisoblash uchun map va lambda funksiyalaridan foydalaning.

sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
juftsonlar = list(filter(lambda x: x%2==0, sonlar))
jsonkvsi = list(map(lambda k: k*k, juftsonlar))
print(jsonkvsi)


#chatgpt bergan alternativ yechim:
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# jsonkvsi = list(map(lambda k: k*k, filter(lambda x: x%2==0, sonlar)))
# print(jsonkvsi)
