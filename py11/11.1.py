def wczytaj_tabl_l(wymiar):
    tab = []
    for i in range(wymiar):
        i_string = str(i)
        nap = "Podaj element nr "+i_string+": "
        tab.append(float(input(nap)))
    return tab     
    
print(wczytaj_tabl_l(3))
