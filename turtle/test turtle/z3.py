from turtle import *

def gwiazdka():
    lt(90)
    width(3)
    for i in range(3):
        pendown()
        fd(0.6*20)
        penup()
        lt(120)
        fd(0.3*20)
        lt(120)
    rt(90)

def siatka(wiersze, kolumny,odstep):
    for i in range(wiersze):
        for i in range(kolumny):
            gwiazdka()
            fd(odstep)
        up()
        bk(odstep*kolumny)
        rt(90)
        fd(odstep)
        lt(90)
    

siatka(5,3,50)
done()
