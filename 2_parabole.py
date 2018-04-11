from calkaOznaczona import calka


def roznica_funkcji(a1, a2, a3, b1, b2, b3):
    return a1-b1, a2-b2, a3-b3


def pole(a1, a2, a3, b1, b2, b3):
    a, b, c = roznica_funkcji(a1, a2, a3, b1, b2, b3)

    sqrt_delta = ((b**2) - (4*a*c))**(1/2)

    if(sqrt_delta <= 0 or a == 0):
        return 0

    x1 = ((-b - sqrt_delta)/(2 * a))
    x2 = ((-b + sqrt_delta)/(2 * a))

    def f(x):
        return((a * (x**2)) + (b*x) + c)

    return abs(calka(f, x1, x2, 1000))


print(pole(1, 3, 6, 1, 3, 3))
