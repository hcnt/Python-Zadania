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

def zmien_gracz(gracz):
    if gracz == 0:
        gracz = 1
    else:
        gracz = 0
    return gracz

def czy_jest_perskie_oczko(tura,punkty):
    if tura == 2 and punkty == 22:
        print("Perskie oczko, Gratulacje, gracz",gracz,"wygrał")
        return True
    return False


punkty[0,0]
gracz = 0
tura = 0

while (punkty[0] < 21 and punkty[1] < 21):
    tura +=1
    print("Gracz",gracz)
    wybor = input("czy chcesz wybrać kolejną karte? T/n: ")
    if (wybor != "T"):
        print("Wynik końcowy gracza",gracz,"to",punkty[gracz])
        break

    punkty[gracz] = dolosuj_karte(punkty[gracz])
    print("twoje punkty to",punkty[gracz])
    print()

    if punkty[gracz] > 21:
        print("Przegrałeś")

    mien_gracz(gracz)


    



