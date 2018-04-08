def suma_cyfr(n):
    sum=0
    while n>0:
        sum += n%10
        n=n//10
    return sum

def kod_poprawny(k):
    ostatnia_cyfra = k%10
    k=k//10
    if ostatnia_cyfra -3 == suma_cyfr(k)%6:
        return True
    else:
        return False
    

print(kod_poprawny(63))
