# Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing.
import re

matn = "Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI. Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"
andoza = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'

linklar = re.findall(andoza, matn)

# Topilgan tuple'larni to'liq URL'ga aylantirish
toliq_linklar = [''.join(link) for link in linklar]

if toliq_linklar:
    print(f"Linklar: {', '.join(toliq_linklar)}")
else:
    print("Linklar yo'q")
    
    
#kod to'gri ishlamaydi, yechimni topolmadim