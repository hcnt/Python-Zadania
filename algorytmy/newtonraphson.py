def sqrt(liczba, epsilon):
    a= 1
    b= liczba
    while(abs(a-b)>epsilon):
        a = (a+b)/2
        b = liczba/a

    return a

def sqrt_reku(liczba, epsilon):
    def reku1(x,a,b,epsilon):
        if(abs(a-b)<epsilon):
            return a
        else:
            return reku1(x,((a+b)/2),(x/a),epsilon)
        
    return reku1(liczba,liczba,1,epsilon)


def funkcja(x):
    return (x**3) - 2
