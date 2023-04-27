import random

los = (random.randint(0,100))



liczba = int(input("Podaj i zgadnij wylosowaną liczbę: "))
print(los)
while True:
    if los < liczba:
        print ("Wylosowana liczba jest mniejsza")
        liczba = int(input("Podaj inną liczbę: "))
    elif los > liczba:
        print ("Wylosowana liczba jest większa")
        liczba = int(input("Podaj inną liczbę:  "))
    else:
        print ("Brawo ! Zgadłeś/aś liczbę!")
        break


