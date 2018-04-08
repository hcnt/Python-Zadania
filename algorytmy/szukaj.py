def szukaj_liczby(tab,a,b,cyfra):     
    index = (a+b)//2
    while(b>=a):
        index = (a+b)//2
        if tab[index] < cyfra:
            a = index+1
        elif tab[index] > cyfra:
            b = index-1
        else:
            return index
    return -1

tablica = [1,6,7,25,65,99,100]


def szukaj_reku(tab,a,b,liczba):
    index = (a+b)//2
    if b<a:
        return -1
    elif tab[index] == liczba:
        return index
    elif tab[index] < liczba:
        return szukaj_reku(tab,index+1,b,liczba)
    elif tab[index] > liczba:
        return szukaj_reku(tab,a,index-1,liczba)           


print(szukaj_reku(tablica,0,len(tablica),1))
