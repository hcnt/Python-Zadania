def liczba_dzielnikow(n, a, b):
    l=0
    for i in range (a,b+1):
       if n%i==0:
           l+=1
    return l

print(liczba_dzielnikow(5, 1, 5))
