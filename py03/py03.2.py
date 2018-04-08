a = int(input("podaj liczbę całkowitą: "))
if(a<0 and a>9999):
    print("podaj liczbe od 0 do 9999")
else:
    print("liczba jedności to", a%10)
    print("liczba dziesiątek to", int((a%100-a%10)/10))
    print("liczba setek to", int((a%1000-a%100)/100))
    print("liczba tysięcy to", int((a%10000-a%1000)/1000))
