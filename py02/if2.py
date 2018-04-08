a = float(input("Podaj pierwszą liczbę rzeczywistą: "))
b = float(input("Podaj drugą liczbę rzeczywistą: "))
c = float(input("Podaj trzecią liczbę rzeczywistą: "))

if a>=b:
    if a>=c:
        print(a)
if b>=c:
    print(b)
elif c>b:
    print(c)
