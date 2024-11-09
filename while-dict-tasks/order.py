#order-oluvchi
orders=[]
while True :
   order=input('Nima buyurtma qilasiz: ')
   orders.append(order)
   print(f"Sizning buyurtlaringiz:\n {orders}")
   javob = input("\nYana mahsulot qo\'shasizmi?(ha/yo\'q): ")
   if javob != 'ha':
        break