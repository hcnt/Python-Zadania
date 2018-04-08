from random import *
def losuj(n, a, b):
    tab = []
    tab.append(randint(a,b))
    while len(tab)<n:
        los = randint(a,b)
        if tab[-1] <= los:
            tab.append(los)
        
    return tab

print(losuj(3,1,6))
print(losuj(2,5,6))
