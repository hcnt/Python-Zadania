a = int(input("podaj wysokość górnej części"))
b = int(input("podaj wysokość donlej z poprzeczką"))
x=0

print(" "*(a+b-1) + "*")

for i in range(a-1):
    print(" "*(a+b-i-2)+"*"+" "*(x+1)+"*")
    x+=2
print(" "*(b-1)+"*"+"*"*(x+1)+"*")

for i in range(b-1):
    print(" "*(b-i-2)+"*"+" "*(x+3)+"*")
    x+=2




