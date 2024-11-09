#order-oluvchi
orders=[]
products={'osh': 10,
          'qovun': 3,
          'tarvuz': 4,
          'kabob': 8,
          'baliq': 15, 
          'ot': 20}
while True :
   order=input('Nima buyurtma qilasiz: ')
   orders.append(order)
   if order in products.keys():
       print(f"{order}ning narxi: {products[order]} so'm")
   else:
       print(f"{order} mahsuloti bizda yo'q")
   javob = input("Yana biror nima xohlaysizmi? (ha/yo\'q): \n> ")
   if javob != 'ha':
        break