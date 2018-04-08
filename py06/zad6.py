x=0
while x<=0:
    x = int(input("Podaj liczbe: "))

a=0
i=10
if a==1:
    print(1)
else:
    while i<10*x:
        a+=((x%i-x%(i/10))/(i/10))
        i*=10
    print(a)