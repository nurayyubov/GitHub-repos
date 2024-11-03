mahsulotlar = ['non', 'sabzi', 'suv', 'yogurt', 'banan', 'don', 'un', 'sok', 'ww', 'qq']
savat = []
bor_mahsulotlar = []
yoq_mahsulotlar = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else: 
        yoq_mahsulotlar.append(mahsulot)
if len(yoq_mahsulotlar)==0:
    print('siz soragan hamma narsa bor')
else:
    print('quyidagi mahsulotlar yoq: ', yoq_mahsulotlar)
    