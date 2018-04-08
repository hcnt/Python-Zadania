a = float(input("podaj 1 bok: "))
b = float(input("podaj 2 bok: "))
c = float(input("podaj 3 bok: "))

if(a>0 and b>0 and c>0):
        if a+b>c:
                if a+c>b:
                        if b+c>a:
                                p = (1/2)*(a+b+c)
                                pole =(p*(p-a)*(p-b)*(p-c))**(1/2)
                                obw = a+b+c
                                print("liczby mogą być bokami trójkąta")
                                print("jego pole to",pole)
                                print("jego obwód to",obw)
else: 
        print("podane boki nie mogą być bokami trójkąta")
