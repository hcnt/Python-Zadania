a = int(input("podaj wysokość: "))
b = int(input("podaj szerokość: "))

print("*"*b)
for i in range(a-2):
    print("*"+"."*(a-2)+"*")
print("*"*b)
