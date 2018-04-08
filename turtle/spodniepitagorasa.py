from turtle import *
from math import atan,degrees,sqrt

def square(r):
    pendown()
    for i in range(4):
        fd(r)
        lt(90)
    penup()


def spodnie_pitagorasa(a,b):
    alfa = degrees(atan(b/a))
    c = sqrt(a**2+b**2)
    square(c)
    rt(90+alfa)
    square(a)
    lt(90)
    fd(a)
    square(b)
    
spodnie_pitagorasa(90,70)
