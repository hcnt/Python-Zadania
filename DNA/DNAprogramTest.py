from dnaLib import *
from DNAprogram import *

def mainTest(lancuch,typ,nr_w_lancuchu,zasada):
    lancuch = lancuch.upper()
    if (czy_DNA(lancuch)):
        lancuch = DNA_na_RNA(lancuch)
    elif(not czy_RNA(lancuch)):
        print("Błąd, nie podano prawidłowego łancucha, spróbuj jeszcze raz")
        return 0

    czySzkodliwy = szkodliwoscMutacji(lancuch,typ,nr_w_lancuchu,zasada)
    return czySzkodliwy

def DNAtest(lancuch,typ,nr_w_lancuchu,zasada,prawidlowy_wynik):
    wynik = mainTest(lancuch,typ,nr_w_lancuchu,zasada)
    print(lancuch,typ,nr_w_lancuchu,zasada,"||",wynik, "-", prawidlowy_wynik)
    if (wynik == prawidlowy_wynik):
        print("wynik prawidlowy")
    else:
        print("wynik błędny")


DNAtest("AugUcaCauUaa","substytucja",5,'G',"Mutacja nieszkodliwa")
DNAtest("AugUcaCauUaa","substytucja",4,'U',"Mutacja szkodliwa")
