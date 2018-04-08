
def suma_cyfr(x):
    a=0
    i=10
    if a==1:
        print(1)
    else:
        while i<10*x:
            a+=((x%i-x%(i/10))/(i/10))
            i*=10
        return a

x=0
while x<=0:
    x = int(input("Podaj liczbe: "))

print(suma_cyfr(x))
x = suma_cyfr(x)

while(x>=10):
    print(suma_cyfr(x))
    x = suma_cyfr(x)