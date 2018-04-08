a = int(input("Podaj liczbe całkowitą: "))

l=0
if a == 0:
    print("liczba musi być nie zerowa")
else:
    for i in range(1,a+1):
        if a % i == 0:
            l+=1
print(l)
