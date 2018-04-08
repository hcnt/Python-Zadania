from random import *
tab = []
while(len(tab)<4):
    los = randint(1, 10)
    for i in range(len(tab)):
        if los == tab[i]:
            break
        if i+1 == len(tab):
            tab.append(los)
print(tab)
