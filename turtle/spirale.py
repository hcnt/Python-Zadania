from turtle import *

def spirala(startowy_bok, startowy_kat, przyrost_boku, przyrost_kata, ile_odcinkow):
    for i in range(ile_odcinkow):
        fd(startowy_bok+i*przyrost_boku)
        rt(startowy_kat+i*przyrost_kata)

speed(11)
spirala(10,60,5,0,15)        
spirala(10,90,5,0,14)
spirala(10,0,0,1,500)
spirala(20,120,10,0,15)
