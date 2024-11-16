def calculate_fac(n):
    if n<0:
        return "musbat son kiriting"
    else:
        a=1
        for i in range(1,n+1):
            a*=i
        return a

print(calculate_fac(0))
        
        