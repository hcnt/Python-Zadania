def odwroc(napis):
    odwrocony_napis = ""
    for i in range(len(napis)):
        odwrocony_napis += napis[len(napis)-i-1]
    return odwrocony_napis
    
print(odwroc("jan pawel drugi"))
