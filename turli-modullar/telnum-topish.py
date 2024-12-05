# Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni andoza yordamida tekshiring

import re
telnum = input('telefon raqamingizni kiriting: ')
andoza = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
if re.match(andoza, telnum):
    print("rahmat")
else:
    print('xato')
    
    
    
