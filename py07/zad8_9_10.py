def suma_dzielnikow(m):
    sum = 0;
    for i in range(1,m):
        if m%i ==0:
            sum+=i
    return sum;

def czy_doskonala(m):
    if m == suma_dzielnikow(m):
        return True
    else:
        return False

def czy_zaprzyjaznione(m, n):
    if suma_dzielnikow(m)==n and suma_dzielnikow(n)==m: 
        return True
    else:
        return False

print(suma_dzielnikow(28)) #28
print(suma_dzielnikow(4))  #3

print(czy_doskonala(28)) #true
print(czy_doskonala(8))  #false

print(czy_zaprzyjaznione(220,284)) #true
print(czy_zaprzyjaznione(8,9))  #false