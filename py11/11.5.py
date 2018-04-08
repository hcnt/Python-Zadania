def przeplec(napis, refren):
    przepleciony_napis = ""
    if len(napis) == 0:
        return ""

    for i in range(len(napis)-1):
        przepleciony_napis += napis[i]+refren

    przepleciony_napis += napis[len(napis)-1]

    return przepleciony_napis
    
print(przeplec("napis", "."))
