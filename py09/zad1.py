rzedy = [1,2,5,7]
gracz = 1

def wyswietl_stan_gry(rzedy,gracz):
    print()
    print()
    print("Liczba pionów w kolejnych rzędach:", rzedy7[0], rzedy[1],rzedy[2],rzedy[3])
    print("")
    print("")
    print("Gracz",gracz,":")

def nie_koniec_gry(rzedy):
    for i in range (4):
        if rzedy[i] != 0:
    return False

def spytaj_o_ruch():
    nr_kupki = int(input("-- z którego rzędu bierzesz piony: "))
    liczba_kamieni = int(input("-- ile pionów bierzesz: "))

    return nr_kupki,liczba_kamieni


def ruch_niepoprawny(rzedy,nr_kupki,liczba_kamieni):
    if nr_kupki<=0 or nr_kupki>4 or liczba_kamieni <= 0:
        return True
    if rzedy[nr_kupki-1] < liczba_kamieni:
        return True
    return False

def komunikat_o_bledzie():
    print("BŁĄD! Nie ma tylu pionów lub takiego rzędu!")
    print()
    print()

def wykonaj_ruch(rzedy,nr_kupki,liczba_kamieni):
    rzedy[nr_kupki-1] -= liczba_kamieni
    return rzedy

def zmien_gracz(gracz):
    if gracz == 1:
        gracz = 2
    else:
        gracz = 1
    return gracz

def komunikat_o_wygranej(gracz):
    print()
    print()
    if gracz == 1:
        print("Przegrał gracz 2...")
    else:
        print("Przegrał gracz 1...")

while nie_koniec_gry(rzedy):
    wyswietl_stan_gry(rzedy,gracz)
    nr_kupki, liczba_kamieni = spytaj_o_ruch()
    while ruch_niepoprawny(rzedy, nr_kupki, liczba_kamieni):
        komunikat_o_bledzie()
        nr_kupki, liczba_kamieni = spytaj_o_ruch()

    rzedy = wykonaj_ruch(rzedy, nr_kupki, liczba_kamieni)
    gracz = zmien_gracz(gracz)

komunikat_o_wygranej(gracz)
done()
