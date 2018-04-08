from random import *
los = randint(1, 1000)
x=0
i=0
while x!=los:
    i+=1
    x=int(input("podaj liczbe: "))
    if x>los:
        print("Podałeś za dużo!")
    elif x<los:
        print("Podałeś za mało!")
    else:
        print("Gratulacje, zgadłeś w",i,"próbie")



