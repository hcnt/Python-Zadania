from random import *
def losuj(n, a, b):
    tab = []
    while len(tab)<n:
        los = randint(a,b)
        if los not in tab:
            tab.append(los)
    return tab

print(losuj(3,1,6))
print(losuj(1,5,6))
