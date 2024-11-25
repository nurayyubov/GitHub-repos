def talabainfo(ism, familiya, **kwargs):
    talaba={'ism':ism, 'familiya':familiya}
    talaba.update(kwargs)
    return talaba
print(talabainfo('Ali', 'Valiyev', tyil=2004, hobby='futbol'))
