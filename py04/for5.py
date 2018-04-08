import math

a = float(input("Podaj początek przedziału: "))
b = int(input("Podaj liczbę podprzedziałów: "))
c = float(input("Podaj długość podprzedziału: "))

for i in range(b):
    print(math.sin(a+(i*c)))

