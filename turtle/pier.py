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

def warstwa_2(il_c,wys_c,szer_c):
    cegla(wys_c,szer_c-(szer_c/2))
    fd(szer_c-(szer_c/2))
    warstwa(il_c,wys_c,szer_c)
    cegla(wys_c,szer_c-(szer_c/2))
    fd(szer_c-(szer_c/2))

def go_back(l_down,l_back):
    rt(90)
    fd(l_down)
    rt(90)
    fd(l_back)
    lt(180)

def piramida(l_r,h_c,w_c):
    for i in range(r_h):
        warstwa(i+1,h_c,w_c)
        rt(90)
        fd(h_c)
        rt(90)
        fd(w_c*(i+1)+w_c/2)
        lt(180)

def mur(il_w,il_c,wys_c,szer_c):
    if il_w%2==0:
        for i in range(int(il_w/2)):
            warstwa(il_c,wys_c,szer_c)
            go_back(wys_c,szer_c*il_c)
            warstwa_2(il_c-1,wys_c,szer_c)
            go_back(wys_c,szer_c*il_c)
    else:
        for i in range(int((il_w-1)/2)):
            warstwa(il_c,wys_c,szer_c)
            go_back(wys_c,szer_c*il_c)
            warstwa_2(il_c-1,wys_c,szer_c)
            go_back(wys_c,szer_c*il_c)
        warstwa(il_c,wys_c,szer_c)

speed(10)
mur(6,5,20,30)
