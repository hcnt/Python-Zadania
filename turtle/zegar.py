from turtle import *
from math import pi
def przejscie(r):
    penup()
    rt(90)
    fd(r)
    lt(90)
    pendown()

def zegar (godzina, minuta, dl_wsk_godz, szer_wsk_godz, dl_wsk_min,szer_wsk_min, promien, dl_podz_godz, dl_podz_min, margines):
    speed(11)
    przejscie(promien)
    circle(promien)
    podzialki(promien,margines,dl_podz_godz,dl_podz_min)
    wskazowki(godzina, minuta, dl_wsk_godz, szer_wsk_godz, dl_wsk_min,szer_wsk_min)


def podzialki(promien,margines,dl_godz,dl_min):
    lt(90)
    penup()
    fd(promien)
    for i in range(60):
        fd(promien-dl_min-margines)
        pendown()
        fd(dl_min)
        penup()
        rt(180)
        fd(promien-margines)
        rt(180)
        rt(360/60)
    for i in range(12):
        fd(promien-dl_godz-margines)
        pendown()
        fd(dl_godz)
        penup()
        rt(180)
        fd(promien-margines)
        rt(180)
        rt(360/12)

def wskazowki(godzina, minuta, dl_wsk_godz, szer_wsk_godz, dl_wsk_min,szer_wsk_min):
    pendown()
    rt((360/12)*godzina)
    width(szer_wsk_godz)
    fd(dl_wsk_godz)
    penup()
    rt(180)
    fd(dl_wsk_godz)
    rt(180)

    pendown()
    rt((360/60)*minuta)
    width(szer_wsk_min)
    fd(dl_wsk_min)
    penup()
    rt(180)
    fd(dl_wsk_min)
    rt(180)

zegar(1,20,40,5,50,3,90,5,2,10)    

