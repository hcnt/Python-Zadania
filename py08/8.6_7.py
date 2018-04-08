def liczba_dzielnikow_wspolnych(n, m, a, b):
    l=0
    for i in range(a,b):
        if n%i==0 and m%i==0:
            print("wspólnym dzielnikiem jest",i)
            l+=1
    return l




def liczba_dzielnikow_osobnych(n, m, a, b):
    l=0
    for i in range(a,b):
        if (n%i==0 and m%i!=0) or (n%i!=0 and m%i==0):
            print("osobnym dzielnikiem jest",i)
            l+=1
    return l


print(liczba_dzielnikow_wspolnych(10,20,1,20))
print(liczba_dzielnikow_osobnych(10,20,1,20))












