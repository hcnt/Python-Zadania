import math

a = float(input("podaj 1 bok: "))
b = float(input("podaj 2 bok: "))
alfa = float(input("podaj kąt: "))
c=0
if(a>0 and b>0 and alfa>0 and alfa<180):
    c = ((b*b+a*a)-(2*a*c*math.cos(math.radians(alfa))))**(1/2)
    p = (1/2)*(a+b+c)
    pole =(p*(p-a)*(p-b)*(p-c))**(1/2)
    obw = a+b+c
    print("c=",c)
    print("jego pole to",pole)
    print("jego obwód to",obw)
else: 
    print("podane boki nie mogą być bokami trójkąta")
