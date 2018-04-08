def znajdz(tablica, element):
    for i in range(len(tablica)):
        if tablica[i] == element:
            return i

    return None
    
print(znajdz([6,4,31,35,64], 67))
