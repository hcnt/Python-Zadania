def wczytaj_tabl_n(wymiar):
    tab = []
    for i in range(wymiar):
        i_string = str(i)
        nap = "Podaj element nr "+i_string+": "
        tab.append(input(nap))
    return tab     
    
print(wczytaj_tabl_n(3))
