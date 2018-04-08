a = int(input("Podaj liczbe całkowitą: "))

l=0
if a == 0:
    print("liczba musi być nie zerowa")
else:
    for i in range(1,a+1):
        if a % i == 0:
            l+=1
if l==2:
    print("liczba jest liczbą pierwszą")
else:
    print("liczba nie jest pierwsza")
