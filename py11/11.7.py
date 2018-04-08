def fragment(napis, znak):
    nowy_napis =""
    poczatek = 0
    koniec = 0
    for i in range(len(napis)):
        if napis[i] == znak:
            poczatek = i
            break
    for i in range(len(napis)-1,0,-1):
        if napis[i] == znak:
            koniec = i
            break
    #print(poczatek,koniec)
    for i in range(poczatek+1,koniec):
        nowy_napis +=napis[i]

    return nowy_napis
    
print(fragment("heheh", "h"))
