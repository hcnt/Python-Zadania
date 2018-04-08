from dnaLib import *



def pobranieMutacji():

    nr_w_lancuchu = int(input("podaj numer zasady do mutacji: "))
    typ = input("podaj typ mutacji (insercja,delecja,substytucja): ")
    zasada = ''

    if (typ == "insercja" or typ =="substytucja"):
        zasada = input("podaj zasade którą chcesz włożyć do łańcucha (A/C/T/G): ")
        return typ,nr_w_lancuchu,zasada

    return typ,nr_w_lancuchu,""

def szkodliwoscMutacji(lancuch,typMutacji,index,zasada):
    zmutowanyLancuch = lancuch
    if (typMutacji == "delecja"):
        zmutowanyLancuch = delecja(lancuch,index)
    elif (typMutacji == "insercja"):
        zmutowanyLancuch = insercja(lancuch,index,zasada)
    elif (typMutacji == "substytucja"):
        zmutowanyLancuch = substytucja(lancuch,index,zasada)

        print(na_bialko(lancuch))
        print(na_bialko(zmutowanyLancuch))
    if(na_bialko(lancuch) == na_bialko(zmutowanyLancuch)):
        return "Mutacja nieszkodliwa"
    return "Mutacja szkodliwa"



def main():
    czyLancuchJestBłędny = True
    while(czyLancuchJestBłędny): #while(True)
        czyLancuchJestBłędny = True
        lancuch = input("Podaj lancuch: ")
        lancuch = lancuch.upper()
        if (czy_DNA(lancuch)):
            lancuch = DNA_na_RNA(lancuch)
            czyLancuchJestBłędny = False #break;
        elif(czy_RNA(lancuch)):
            czyLancuchJestBłędny = False #break;
        else:
            print("Błąd, nie podano prawidłowego łancucha, spróbuj jeszcze raz")
            print()

    typ,nr_w_lancuchu,zasada = pobranieMutacji()

    czySzkodliwy = szkodliwoscMutacji(lancuch,typ,nr_w_lancuchu,zasada)
    print(czySzkodliwy)

    if(input("Czy chcesz sprawdzić kolejny łańcuch? t/n: ") == 't'):
        main()

#main()
