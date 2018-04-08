from random import *

def rzut_koscmi(n, k):
    sum = 0
    for i in range(n):
        sum+=randint(1,k)
    return sum

def rzut_koscmi_premiowa(k):
    sum=0
    pierwszy_rzut = randint(1,k)
    rzut = pierwszy_rzut
    sum+= pierwszy_rzut
    print("pierwszy rzut:",pierwszy_rzut)
    while rzut == pierwszy_rzut:
        rzut=randint(1,k) 
        if rzut == pierwszy_rzut:
            sum+= rzut
            print("kolejny rzut:", rzut)
    return sum

def rzut_koscmi_premiowymi(n, k):
    sum = 0
    for i in range(n):
        sum+=rzut_koscmi_premiowa(k)
    return sum


print(rzut_koscmi_premiowymi(2,6))
