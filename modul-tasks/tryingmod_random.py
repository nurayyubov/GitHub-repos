# random modulidan foydalanib quyidagilarni bajaring:
# 1. 1 dan 100 gacha tasodifiy raqamni chop eting.
# 2. 'python', 'java', 'c++', 'javascript' ichidan tasodifiy birini tanlang.
# 3. Berilgan ro'yxatni aralashtiradigan dastur yozing.

import random as r
#1
print(r.randint(1,100))
#2
print(r.choice(['python', 'java', 'c++', 'javascript']))
#3
languages = ['python', 'java', 'c++', 'javascript']
r.shuffle(languages)
print(languages)   

