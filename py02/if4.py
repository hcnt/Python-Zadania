a = float(input("Podaj pierwszą liczbę rzeczywistą: "))
b = float(input("Podaj drugą liczbę rzeczywistą: "))
c = float(input("Podaj trzecią liczbę rzeczywistą: "))
d = float(input("Podaj czwartą liczbę rzeczywistą: "))
 
if a>b:
    k=b
    b=a
    a=k
if a>c:
    k=c
    c=a
    a=k
if a>d:
    k=a
    a=a
    a=k
if b>c:
    k=c
    c=b
    b=k
if c>d:
    k=d
    d=c
    c=k

print(d,c,b,a)
    
    
