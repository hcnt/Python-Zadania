from random import *

def dolosuj_karte(punkty):
    n = randint(1,12)
    karta="karta"
    if n==1:
        karta = "dwa"
        punkty+=2
    elif n==2:
        karta = "trzy"
        punkty+=3
    elif n==3:
        karta = "cztery"
        punkty+=4
    elif n==4:
        karta = "pięć"
        punkty+=5
    elif n==5:
        karta = "sześć"
        punkty+=6
    elif n==6:
        karta = "siedem"
        punkty+=7
    elif n==7:
        karta = "osiem"
        punkty+=8
    elif n==8:
        karta = "dziewięć"
        punkty+=9
    elif n==9:
        karta = "dziesięć"
        punkty+=10
    elif n==10:
        karta = "walet"
        punkty+=2
    elif n==11:
        karta = "dama"
        punkty+=3
    elif n==12:
        karta = "król"
        punkty+=4
    elif n==13:
        karta = "as"
        punkty+=11
    print("wylosowana karta to",karta)
    return punkty

punkty = 0
punkty = dolosuj_karte(punkty)
print("twoje punkty to",punkty)
tura = 1
while (punkty < 21):
    tura+=1
    wybor = input("czy chcesz wybrać kolejną karte? T/n: ")
    if (wybor != "T"):
        print("twój wynik to",punkty)
        break
    punkty = dolosuj_karte(punkty)
    if tura == 2 and punkty == 22:
        print("Perskie oczko, Gratulacje, wygrałeś")
        break

    print("twoje punkty to",punkty)
    print()
    if punkty > 21:
        print("Przegrałeś")
    



