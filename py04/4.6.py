a = int(input("podaj wysokość"))

x=1
for i in range(a):
    print(" "*(a-i-1)+"*"*(x))
    x+=2
