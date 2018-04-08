a = int(input("Podaj liczbe całkowitą: "))
b = int(input("Podaj liczbe całkowitą: "))
x = float(input("Podaj liczbe rzeczywistą: "))
y = float(input("Podaj liczbe rzeczywistą: "))


suma=0
for i in range(a,b+1):
    suma += ((x-i)/(y+i))

print(suma)
