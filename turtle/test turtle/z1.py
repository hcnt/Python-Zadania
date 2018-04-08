from turtle import *

def pien(szer_pnia, wys_pnia):
    fillcolor(0.3,0,0)
    begin_fill()
    lt(90)
    fd(wys_pnia)
    rt(90)
    fd(szer_pnia)
    rt(90)
    fd(wys_pnia)
    rt(90)
    fd(szer_pnia)
    rt(90)
    end_fill()
    fd(wys_pnia)
    lt(90)

def przejscie(szer_pnia,rozmiar):
    up()
    rt(90)
    fd(rozmiar*0.6)
    rt(90)
    fd((rozmiar/2)-(szer_pnia/2))
    lt(180)


def trojkat(szer_pnia,rozmiar):
    color(0,0.7,0)
    begin_fill()
    fd((rozmiar/2)-(szer_pnia/2))
    rt(120)
    fd(rozmiar)
    rt(120)
    fd(rozmiar)
    rt(120)
    fd(rozmiar)
    end_fill()

def choinka(szer_pnia, wys_pnia, rozmiar):

    pien(szer_pnia, wys_pnia)
    
    trojkat(szer_pnia,rozmiar)

    przejscie(szer_pnia,rozmiar)
    trojkat(szer_pnia,rozmiar*0.8)

    przejscie(szer_pnia,rozmiar*0.8)
    trojkat(szer_pnia,rozmiar*0.4)


choinka(10,40,100)

done()
