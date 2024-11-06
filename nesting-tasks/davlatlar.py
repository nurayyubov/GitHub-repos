davlatlar = {
    "o\u02BBzbekiston": {'poytaxt': "toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }

for davlat in davlatlar:
   poytaxt = davlatlar[davlat]['poytaxt']
   maydon = davlatlar[davlat]['maydon']
   aholi = davlatlar[davlat]['aholi']
   pul = davlatlar[davlat]['pul birligi']
   print(f"\n{davlat.title()} davlatining poytaxti {poytaxt.title()}. "
          f"Maydoni {maydon}, aholisi {aholi} kishi va "
          f"pul birligi {pul}.")
   