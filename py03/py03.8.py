import math

a1 = float(input("podaj 1 parametr 1 równania: "))
b1 = float(input("podaj 2 parametr 1 równania: "))
c1 = float(input("podaj prawą strone 1 równania: "))
a2 = float(input("podaj 1 parametr 2 równania: "))
b2 = float(input("podaj 2 parametr 2 równania: "))
c2 = float(input("podaj prawą strone 2 równania: "))

w= (a1*b2)-(a2*b1) 
wx=(c1*b2)-(c2*b1)
wy=(a1*c2)-(a2*c1)
if (w == 0 and wx==0 and wy==0):
    print("układ nieoznaczony")
elif(w ==0 and (wx!=0 or wy!=0)):
    print("układ sprzeczny")
else:
    print("x=",wx/w)
    print("y=",wy/w)


