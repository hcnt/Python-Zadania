def czy_DNA(napis):
    zasady = ["A","T","C","G"]
    for i in range(len(napis)):
        if napis[i] not in zasady:
            return False
    return True

def czy_RNA(napis):
    zasady = ["A","U","C","G"]
    for i in range(len(napis)):
        if napis[i] not in zasady:
            return False
    return True

def zamien(znak1,znak2,napis):
    napis = list(napis)
    for i in range(len(napis)):
        if napis[i] == znak1:
            napis[i] = znak2
        elif napis[i] == znak2:
            napis[i] = znak1
    return ''.join(napis)


def dopelnienie_DNA(napis):
    pary = [['A','T'],['C','G']]
    napis = zamien(pary[0][0],pary[0][1],napis)
    napis = zamien(pary[1][0],pary[1][1],napis)
    return napis


def DNA_na_RNA(napis):
    para = ["T","U"]
    napis = zamien(para[0],para[1],napis)
    return napis

def RNA_na_DNA(napis):
    para = ["U","T"]
    napis = zamien(para[0],para[1],napis)
    return napis

def na_kodony(napis):
    kodony = []
    kodon = ''
    for i in range(len(napis)):
         kodon += (napis[i])
         if(len(kodon) == 3 or i == len(napis)-1):
             kodony.append(kodon)
             kodon =''
    return kodony


def insercja(lancuch, nr_w_lancuchu,zasada):
    pom = list(lancuch)
    pom.insert(nr_w_lancuchu,zasada)
    return ''.join(pom)

def delecja(lancuch, nr_w_lancuchu):
    pom = list(lancuch)
    pom.pop(nr_w_lancuchu)
    return ''.join(pom)

def substytucja(lancuch, nr_w_lancuchu,zasada):
    pom = list(lancuch)
    pom[nr_w_lancuchu] = zasada
    return ''.join(pom)


def na_aminokwasy(kodony):

    lancuch = []
    for i in range(len(kodony)):
        if(kodony[i] == 'UUU' or kodony[i] == 'UUC'):
            lancuch.append("Phe")
        elif(kodony[i] == 'UUA' or kodony[i][0:2] == 'CU'):
            lancuch.append("Leu")
        elif(kodony[i][0:2] == 'AU' and kodony[i][2] != 'G'):
            lancuch.append("Ile")
        elif(kodony[i] == 'AUG'):
            lancuch.append("Met")
        elif(kodony[i][0:2] == 'GU'):
            lancuch.append("Val")
        elif(kodony[i][0:2] == 'UC'):
            lancuch.append("Ser")
        elif(kodony[i][0:2] == 'CC'):
            lancuch.append("Pro")
        elif(kodony[i][0:2] == 'AC'):
            lancuch.append('Thr')
        elif(kodony[i][0:2] == 'GC'):
            lancuch.append('Ala')
        elif(kodony[i] == 'UAU' or kodony[i] == 'UAC'):
            lancuch.append('Tyr')
        elif(kodony[i] == 'UAA' or kodony[i] == 'UAC'or kodony[i] == 'UGA'):
            lancuch.append("STOP")
        elif(kodony[i] == 'CAU' or kodony[i] == 'CAC'):
            lancuch.append('His')
        elif(kodony[i] == 'CAA' or kodony[i] == 'CAG'):
            lancuch.append('Gln')
        elif(kodony[i] == 'AAU' or kodony[i] == 'AAC'):
            lancuch.append('Asn')
        elif(kodony[i] == 'AAA' or kodony[i] == 'AAG'):
            lancuch.append('Lys')
        elif(kodony[i] == 'GAU' or kodony[i] == 'GAC'):
            lancuch.append('Asp')
        elif(kodony[i] == 'GAA' or kodony[i] == 'GAG'):
            lancuch.append('Glu')
        elif(kodony[i] == 'UGU' or kodony[i] == 'UGC'):
            lancuch.append('Cys')
        elif(kodony[i] == 'UGG'):
            lancuch.append('Trp')
        elif(kodony[i][0:2] == 'CG' or kodony[i] == 'AGA' or kodony[i] == 'AGG'):
            lancuch.append('Arg')
        elif(kodony[i] == 'AGU' or kodony[i] == 'AGC'):
            lancuch.append('Ser')
        elif(kodony[i][0:2] == 'GG'):
            lancuch.append('Gly')

    return lancuch

def na_bialko(lancuch):

    if (czy_DNA(lancuch)):
        lancuch = DNA_na_RNA(lancuch)
    lancuch = na_kodony(lancuch)
    lancuch = na_aminokwasy(lancuch)

    #print(lancuch)
    if ('STOP' not in lancuch or 'Met' not in lancuch):
        return ''

    start = lancuch.index('Met')

    stop = lancuch.index('STOP')

    bialko = lancuch[start+1:stop]

    return bialko



def napis_test(funkcja,napis,wynik):
    print(napis,"-->", funkcja(napis),"prawidłowy wynik to",wynik)
    if funkcja(napis) == wynik:
        print("wynik prawidlowy")
    else:
        print("wynik błędny")

# napis = "UUUUUAUUCAUGUGCAUGUGUUAA"
# ##
# ##print(napis)
# print(na_bialko(napis));

#napis_test(czy_DNA,"ACTG",True)

##napis_test(dopelnienie_DNA,"ATCGATCG","TAGCTAGC")

##napis_test(DNA_na_RNA,"ATCGATCG","AUCGAUCG")

##napis_test(na_kodony,"ATCGATCG",["ATC","GAT","CG"])
