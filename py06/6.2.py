a = int(input("Podaj liczbe całkowitą: "))
while a<2:
    a = int(input("Podaj liczbe większą od 2: "))

l=0

for i in range(1,a+1):
    if a % i == 0:
        l+=1

if l==2:
    print("liczba jest liczbą pierwszą")
else:
    print("liczba nie jest pierwsza")
