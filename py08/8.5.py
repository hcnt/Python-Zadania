from random import *
def losuj_2(n, a, b):
    tab=[]
    print("1 losowanie od",a,"do",b-n+1) 
    tab.append(randint(a,b-n+1))
    print("wynik to",tab[-1])
    for i in range(1,n):
        print("losowanie od", tab[-1]+1,"do",b-(n-i-1))  
        tab.append(randint(tab[-1]+1,b-(n-i-1)))
        print("wynik to",tab[-1])
    return tab


print(losuj_2(5,1,20))

print(losuj_2(2,5,10))












