from turtle import *
import math
speed(50)
def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y

r = 1000
for x in range(0,r): fd(7);left(x**8);color(mapFromTo(math.sin(0.1*x),-1,1,0,1),(mapFromTo(math.sin(0.1*x),-1,1,1,0)),1);print(x);print(mapFromTo(x,0,r,0,1))


