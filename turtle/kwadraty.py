from turtle import *
from random import randint

def cegla(h,w):
    pendown()
    fd(w)
    left(90)
    fd(h)
    left(90)
    fd(w)
    left(90)
    fd(h)
    
    left(90)
    penup()

def warstwa(il_c,wys_c,szer_c):
    for i in range (il_c):
        cegla(wys_c,szer_c)
        fd(szer_c)

def piramida(il_w,wys_c,szer_c):
    for i in range(il_w):
        warstwa(i+1,wys_c,szer_c)
        rt(90)
        fd(wys_c)
        rt(90)
        fd(szer_c*i)
        lt(180)
        
    
piramida(4,20,20)
