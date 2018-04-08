m = int(input("Podaj liczbe całkowitą: "))
n = int(input("Podaj liczbe całkowitą: "))

suma=0.0 
for i in range(m,n+1):
    suma += 1/i

print(suma)
