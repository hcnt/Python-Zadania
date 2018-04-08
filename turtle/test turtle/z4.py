from turtle import *


def platek(kat_luku, promien_luku):

    begin_fill()
    rt(kat_luku/2)
    circle(promien_luku, kat_luku)
    lt(180-kat_luku)
    circle(promien_luku, kat_luku)
    lt(180-kat_luku/2)
    end_fill()

def kolo(promien):
    bk(promien)
    rt(90)
    color(0,0,1)
    begin_fill()
    circle(promien)
    end_fill()

color(1,0,0)
for i in range(5):
    platek(120,90)
    rt(360/5)


kolo(20)
done()
