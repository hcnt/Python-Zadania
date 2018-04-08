def rzymskie(napis):
    liczby =[]
    for i in range(len(napis)):
        if napis[i] == "I":
            liczby.append(1)
        if napis[i] == "V":
            liczby.append(5)
        if napis[i] == "X":
            liczby.append(10)
        if napis[i] == "L":
            liczby.append(50)
        if napis[i] == "C":
            liczby.append(100)
        if napis[i] == "D":
            liczby.append(500)
        if napis[i] == "M":
            liczby.append(1000)
    print(liczby)

    wynik = 0
    for i in range(len(liczby)-1):
        if liczby[i]>=liczby[i+1]:
            wynik+=liczby[i]
            print("liczba",liczby[i],"jest wieksza-równa od",liczby[i+1],"wynik to",wynik)
            if i == len(liczby)-2:
                wynik+=liczby[len(liczby)-1]
        else:
            wynik+=liczby[i+1]-liczby[i]
            print("liczba",liczby[i],"jest mniejsza od",liczby[i+1],"wynik to",wynik)

        print(i)
    return wynik

print(rzymskie("MCMX"))    
#print(rzymski())
