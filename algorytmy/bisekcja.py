
def funkcja(x):
    return (5*x)+5

def bisekcja(f,a,b,epsilon):
    c = (a+b)/2
    if f(c) == 0:
        return c
    while(abs(a-b)>epsilon):
        c = (a+b)/2
        if (f(c)*f(a))<0:
            b = c
        else:
            a = c
    return (a+b)/2

def bisekcja_reku(f,a,b,epsilon):
    c = (a+b)/2
    if f(c) == 0:
        return c
    elif(abs(a-b)<epsilon):
        return (a+b)/2
    elif f(c)*f(a) < 0:
        return(bisekcja_reku(f,a,c,epsilon))
    else:
        return(bisekcja_reku(f,c,b,epsilon))
    


print(bisekcja(funkcja,-5,10,0.00001))

print(bisekcja_reku(funkcja,-5,10,0.00001))

