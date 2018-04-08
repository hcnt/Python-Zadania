
a = float(input("podaj współczynnik a prostej: "))
b = float(input("podaj współczynnik b prostej: "))

if(a>0):
    if(b==0):
        print("przechodzi przez 1 i 3")
    elif(b>0):
        print("przechodzi przez 1, 2 i 3")
    else:
        print("przechodzi przez 1, 3 i 4")
elif(a==0):
    if(b>0):
        print("przechodzi przez 1 i 2 ")
    elif(b<0):
        print("przechodzi przez 3 i 4")
    elif(b==0):
        print("pokrywa się z osią OX")
elif(a<0):
    if(b==0):
        print("przechodzi przez 2 i 4")
    elif(b>0):
        print("przechodzi przez 1, 2 i 4")
    else:
        print("przechodzi przez 2, 3 i 4")
