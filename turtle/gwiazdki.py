from turtle import *

def gwiazdka(n,bok,l_obr):
    for i in range (n):
        fd(bok)
        lt((360/n)*l_obr)

def przejscie(lk,xw,yw):
        up()
        fd(xw)
        rt(90)
        fd(yw)
        lt(90)
        down()

def w_gwiazdek(n,bok,l_obr,lk,xw,yw):
    for i in range (lk):
        gwiazdka(n,bok,l_obr)
        przejscie(lk,xw,yw)
    lt(180)
    for i in range(lk):
        przejscie(lk,xw,yw)
    lt(180)   

def gwiazdki (n,bok,l_obr,lw,lk,xw,yw,xk,yk):
    for i in range(lw):
         w_gwiazdek(n,bok,l_obr,lk,xw,yw)
         up()
         rt(90)
         fd(yk)
         lt(90)
         fd(xk)
         down()


    
    
speed(11)
gwiazdki(5,20,2,3,3,30,10,10,30)

