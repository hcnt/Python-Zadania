from turtle import *


def square(r):
    pendown()
    begin_fill()
    for i in range(4):
        fd(r)
        left(90)
    end_fill()
    penup()
    
def szachownica(lw, lk, wym, kontur, kolor1, kolor2):
    rt(90)
    fd(lw*wym)
    lt(90)
    pencolor(kontur)
    for i in range(lw):
        for j in range(lk):
            if((i+j)%2==0):
                fillcolor(kolor1)
            else:
               fillcolor(kolor2)
            square(wym)
            fd(wym)
        lt(90)
        fd(wym)
        lt(90)
        fd(lk*wym)
        lt(180)
    rt(90)
    fd(lw*wym)
    lt(90)

def pion(w, k, wym, kontur, kolor):
    penup()
    fd((k-1)*wym+(0.5*wym))
    lt(90)
    fd((w-1)*wym+(0.1*wym))
    rt(90)
    pendown()
    pencolor(kontur)
    fillcolor(kolor)
    begin_fill()
    circle(0.8*wym/2)
    end_fill()
    penup()
    rt(90)
    fd((w-1)*wym+(0.1*wym))
    rt(90)
    fd((k-1)*wym+(0.5*wym))
    rt(180)
    
def dama(w, k, wym, kontur, kolor1, kolor2):
    ##penup()
    fd((k-1)*wym+(0.5*wym))
    lt(90)
    fd((w-1)*wym+(0.1*wym))
    rt(90)
    pendown()
    pencolor(kontur)
    fillcolor(kolor1)
    begin_fill()
    circle(0.8*wym/2)
    end_fill()
    penup()
    width(0.1*wym)
    lt(90)
    penup()
    fd(0.1*wym)
    for i in range(3):
        pencolor(kolor2)
        pendown()
        fd(0.6*wym)
        penup()
        lt(120)
        fd(0.3*wym)
        lt(120)
    bk(0.1*wym)
    lt(90)
    fd(wym/4)
    fd((k-1)*wym+(0.25*wym))
    lt(90)
    fd((w-1)*wym+(0.1*wym))
    lt(90)
        
    
    
def test3():

    szachownica(5, 5, 40, "black", "black", "white")

    pion(3, 1, 40, "black", "red")

    pion(3, 5, 40, "black", "red")

    pion(5, 1, 40, "black", "blue")

    dama(3, 3, 40, "black", "red", "yellow")

    dama(1, 5, 40, "black", "blue", "white")

    dama(1, 1, 40, "black", "blue", "white")

    up()

    bk(500)

    down()

    szachownica(7, 15, 30, "red", "yellow", "blue")

    pion(2, 1, 30, "black", "white")

    pion(5, 3, 30, "white", "black")

    dama(2, 11, 30, "black", "white", "purple")

    dama(1, 13, 30, "white", "black", "pink")



reset()

speed(11)

test3()
