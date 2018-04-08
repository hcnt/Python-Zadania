a = int(input("podaj wysokość"))

x=1
for i in range(a):
    print(" "*(a-i-1)+"*"*(x))
    x+=2
x-=2
for i in range(a):
    x-=2
    print(" "*(i+1)+"*"*(x))
