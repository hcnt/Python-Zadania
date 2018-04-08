a = float(input("Podaj pierwszą liczbę rzeczywistą: "))
b = float(input("Podaj drugą liczbę rzeczywistą: "))
c = float(input("Podaj trzecią liczbę rzeczywistą: "))

if((a<=b and a>=c and b>c) or (a>=b and a<=c and b>c)):
    print(a)
elif((b<=a and b>=c and a>c) or (b>=a and b<=c and a>c)):
    print(b)
elif((c<=a and c>=b and b>a) or (c>=a and c<=b and b>a)):
    print(c)
