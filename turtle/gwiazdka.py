from turtle import *

def gwiazdka(n,bok,l_obr):
    for i in range (n):
        fd(bok)
        lt((360/n)*l_obr)
def fraktal(n,bok,l_obr):
    for i in range (n):
        fd(bok)
        lt(36)
        gwiazdka(n,bok/5,l_obr)
        lt((360/n)*l_obr)
        rt(36)
def fraktal2(n,bok,l_obr):
    for i in range (n):
        fd(bok)
        lt(36)
        fraktal(n,bok,l_obr)
        lt((360/n)*l_obr)
        rt(36)
def fraktal3(n,bok,l_obr):
    for i in range (n):
        fd(bok)
        lt(36)
        fraktal2(n,bok,l_obr)
        lt((360/n)*l_obr)
        rt(36)
def fraktal4(n,bok,l_obr):
    for i in range (n):
        fd(bok)
        lt(36)
        fraktal3(n,bok,l_obr)
        lt((360/n)*l_obr)
        rt(36)
#gwiazdka(8,100,1)
#gwiazdka(8,100,3)
#gwiazdka(7,100,3)

#gwiazdka(21,100,5)
#gwiazdka(17,100,9)
speed(11)       
fraktal4(5,50,3)
