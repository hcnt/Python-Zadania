m = int(input("Podaj liczbe całkowitą: "))

suma=0
for i in range(1,m+1):
    suma += (4*i*i)/(4*i*i-1)

print(2*suma)
