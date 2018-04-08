def liczba_kwadratow(a, b):
    l=0
    for i in range (a,b+1):
        if (i**(1/2))%1 == 0:
            l+=1
    return l

print(liczba_kwadratow(9,16)) #10
