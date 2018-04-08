def znajdz_najmn_nat(a, b, c, d, e, f, z):
    wynik = 0
    x=1
    while wynik%z!=0:
        wynik = (a*(x**3))+(b*x*x)+(c*x)+(d*((x+e)**1/2))+f 
        x+=1
    return wynik
