import math as m

def f(x):
    return (abs(x)**(1/2))+(m.sin(x)/(1+(x*x)))

def g(x):
    if x>0:
        return f(x)
    elif (x>=-1 and x<=0):
        return -(abs(f(x)))**(1/3)
    elif x<-1:
        return 0
    
