from turtle import *

def wielokat(ile,bok):
    for i in range (ile):
        fd(bok)
        lt(360/ile)

speed(3)

## kwadraty
wielokat(4,40)

up()
fd(20)
rt(90)
fd(10)
lt(135)
down()

wielokat(4,40)
rt(45)

##przejście
up()
fd(100)
down()

##trójkąty
wielokat(3,40)

up()
rt(30)
fd(22)
lt(90)
down()

wielokat(3,40)
