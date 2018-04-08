month=-1

while(month<1 or month>12):
    month = int(input("Podaj numer miesiąca: "))

year=-1
while year<=0:
    year = int(input("Podaj numer roku: "))
days=0

if (month == 4 or month == 6 or month == 9 or month == 11):
    days = 30;
if month == 2:
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        days=28
    else:
        days =29
else:
    days=31
print("liczba dni w miesiącu",month,"w roku",year,"to",days)
