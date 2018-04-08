a = int(input("podaj wysokość górnej części"))
b = int(input("podaj wysokość donlej z poprzeczką"))
x=0

print(" "*(a) + "*")

for i in range(a-1):
    print(" "*(a-i-1)+"*"+" "*(x+1)+"*")
    x+=2
print("*"+"*"*(x+1)+"*")

for i in range(b-1):
    print("*"+" "*(x+1)+"*")




     
