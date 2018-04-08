def silnia(m):
    if m <=0:
        return 1
    else:
        x=1
        for i in range(1,m+1):
            x*=i
        return x




print(silnia(-10))#1 
print(silnia(0))#1
print(silnia(12))#479001600
print(silnia(4))#24
