a = int(input("Podaj liczbe całkowitą: "))
while a<2:
    a = int(input("Podaj liczbe większą od 0: "))

l=2

while a!=1:
    if a%l==0:
        a=a/l
        print(l)
        l=2
    else:
        l+=1

        
