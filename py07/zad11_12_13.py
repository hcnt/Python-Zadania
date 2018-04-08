def czy_pierwsza(x):
    if x <= 1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True


def liczba_dzielnikow_pierwszych_bp(m):
    l=0
    for i in range(1,m):
        if m%i==0 and czy_pierwsza(i):
            l+=1
    return l

def liczba_dzielnikow_pierwszych_zp(m):
    l=0
    for i in range(1,m):
        if m%i==0 and czy_pierwsza(i):
            k=m
            while k%i==0:
                k=k/i
                l+=1
    return l


def czy_polpierwsza(m):
    if liczba_dzielnikow_pierwszych_zp(m) == 2:
        return True
    else:
        return False



##print(czy_pierwsza(1)) #False
##print(czy_pierwsza(2)) #True
##print(czy_pierwsza(5)) #True
##print(czy_pierwsza(7)) #True
##print(czy_pierwsza(2)) #True
##print(czy_pierwsza(6)) #False

print(liczba_dzielnikow_pierwszych_bp(111)) #2 
print(liczba_dzielnikow_pierwszych_bp(8)) #1 


print(liczba_dzielnikow_pierwszych_zp(8)) #3

print(czy_polpierwsza(26)) # True
print(czy_polpierwsza(11)) # False
