a = float(input("podaj pierwszą liczbe: "))
b = float(input("podaj drugą liczbe: "))
znak = input("podaj działanie (+,-,*,/): ")

if znak == "+":
    print(a,"+",b,"=",a+b)
elif znak == "-":
    print(a,"-",b,"=",a-b)
elif znak == "*":
    print(a,"*",b,"=",a*b)
elif znak == "/":
    if b==0:
        print("dzielenie przez 0")
    else:
        print(a,"/",b,"=",a/b)
else:
    print("nieprawidłowe działanie")
    
