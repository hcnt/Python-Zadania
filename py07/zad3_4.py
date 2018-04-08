def czy_przestepny(rok):
    if ((rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0)):
        return True
    else:
        return False

def liczba_dni(mies,rok):
    if (mies == 4 or mies == 6 or mies == 9 or mies == 11):
        return 30;
    elif mies == 2:
        if czy_przestepny(rok) == True:
            return 28
        else:
            return 29
    else:
        return 30


print(liczba_dni(3,2017))
