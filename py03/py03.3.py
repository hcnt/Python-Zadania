a = float(input("podaj dochód: "))

if a<=85528:
    podatek = ((18/100)*a)-556.02
    if podatek<0:
        podatek=0
else:
    podatek = 14839.02 + (a-85528)*(32/100)

print("podatek to",podatek)

