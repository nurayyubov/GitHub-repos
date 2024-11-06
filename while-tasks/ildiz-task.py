print("Kiritilgan sonning ildizini qaytaruvchi dastur.\n")
print("(dasturni to'xtatish uchun 'exit' deb yozing):\n ")
savol = "Musbat son kiriting> "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng\n")
        
    