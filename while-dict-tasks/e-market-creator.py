products={}
while True:
    prod=input('Mahsulot nomi: ')
    price=input(f"{prod.title()}ning narxi: ")
    products[prod]=int(price)
    flag=input('Yana mahsulot kiritasizmi? (ha\yo\'q) \n> ')
    if flag != 'ha':
        print(F"mahsulotlar: {products}" )
        break
    
    
    {'osh': 10, 'qovun': 3, 'tarvuz': 4, 'kabob': 8}