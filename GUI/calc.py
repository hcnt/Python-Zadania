from plan_ix import Window
okno = Window("Obliczenia")

def dzialanie(app,name,row,col):
    a = float(app.getE("liczba1"))
    b = float(app.getE("liczba2"))

    if(col == 0):
        wynik = a + b
    if(col == 1):
        wynik = a - b
    if(col == 2):
        wynik = a * b
    if(col == 3):
        wynik = a / b
    
    app.config(name = "wynik",text = str(a) + " " + name + " " + str(b) + " = " + str(wynik))
    

def stworzOkno():
    okno.add("L",text="Liczba 1: " ,row = 0, col = 0,colspan = 2)
    okno.add("L",text="Liczba 2: " ,name="xD",row = 1, col = 0,colspan = 2)
    okno.add("E",row = 0,name = "liczba1", col = 2,colspan = 2,width = 8)
    okno.add("E",row = 1,name = "liczba2",  col = 2,colspan = 2,width = 8)
    okno.add("B", text = "+", name = "+",row = 2, col = 0,command = dzialanie,width = 4)
    okno.add("B", text = "-", name = "-",row = 2, col = 1,command = dzialanie,width = 4)
    okno.add("B", text = "*", name = "*",row = 2, col = 2,command = dzialanie,width = 4)
    okno.add("B", text = "/", name = "/",row = 2, col = 3,command = dzialanie,width = 4)
    okno.add("L",text="Wynik",name = "wynik" ,row = 3, col = 0,colspan = 4,width = 25)
    okno.add("L",text=" " ,row = 4, col = 0,colspan = 4,width = 25)


stworzOkno()


