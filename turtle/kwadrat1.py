from turtle import *
from random import randint
import math

def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y

def square(r):
    pendown()
    begin_fill()
    for i in range(4):
        fd(r)
        left(90)
    end_fill()
    penup()

def move(x):
    right(90)
    fd(x)
    left(90)
    fd(x)

reset()
speed(200)
#up()
#left(180)
#fd(250)
#right(180)
#down()
for i in range(-30,30):
    color(mapFromTo(i,-30,30,1,0),mapFromTo(i,-30,30,0,1),mapFromTo(i,-30,30,1,0))
    square(10*math.sin(i))
    move(i/2)

