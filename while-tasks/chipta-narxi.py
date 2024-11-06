print('Chipta narxini aniqlash dasturi! \nDasturni toxtatish uchun quit yoki exit deb yozing')
while True:
    yosh=input('Yoshingizni kiriting:')
    if yosh.lower()=='exit' or yosh.lower()=='quit':
       print('dasturdan chiqildi!')
       break
    yosh=int(yosh)

    if yosh<7:
       narx=2000
    elif 7<=yosh<18:
       narx=3000
    elif 18<=yosh<65:
       narx=10000
    else:
       narx=0

    if narx==0:
       print('sizga bepul')
    else:
       print(f"sizga kirish {narx} so'm")
    
    
