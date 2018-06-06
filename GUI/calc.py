from plan_ix import Window
okno = Window("Obliczenia")


okno.add("L",text="Liczba 1: " ,row = 0, col = 0,colspan = 2)
okno.add("L",text="Liczba 2: " ,row = 1, col = 0,colspan = 2)
okno.add("E",row = 0, col = 2,colspan = 2,width = 8)
okno.add("E",row = 1, col = 2,colspan = 2,width = 8)
okno.add("B", text = "+",row = 2, col = 0)
okno.add("B", text = "-",row = 2, col = 1)
okno.add("B", text = "*",row = 2, col = 2)
okno.add("B", text = "/",row = 2, col = 3)
okno.add("B", text = "/",row = 2, col = 3)
okno.add("L",text="Wynik" ,row = 3, col = 0,colspan = 4)
