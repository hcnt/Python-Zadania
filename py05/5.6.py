a = int(input("Podaj liczbe całkowitą: "))

if a <=0:
    print("liczba musi być dodatnia")
else:
    for i in range(1,a+1):
        if a % i == 0:
            print(i)

