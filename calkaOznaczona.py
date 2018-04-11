def funkcja(x):
    return (x-2)


def calka(f, a, b, ilosc_trapezow):

    epsilon = (b-a)/ilosc_trapezow
    poczatekLiczonegoPrzedzialu = a
    koniecLiczonegoPrzedzialu = a + epsilon

    suma = 0

    for i in range(ilosc_trapezow):

        suma += ((f(poczatekLiczonegoPrzedzialu)
                  + f(koniecLiczonegoPrzedzialu))/2)*epsilon

        poczatekLiczonegoPrzedzialu = koniecLiczonegoPrzedzialu
        koniecLiczonegoPrzedzialu = koniecLiczonegoPrzedzialu + epsilon

    return suma


print(calka(funkcja, 1, 3, 1))
