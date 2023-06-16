import random


while True:
    los = random.randint(0, 100)
    print(los)
    proba = 0

    while True:

        liczba = int(input("Podaj i zgadnij wylosowaną liczbę: "))
        proba += 1

        if los < liczba:
            print("Wylosowana liczba jest mniejsza")
       
       
        elif los > liczba:
            print("Wylosowana liczba jest większa")
       
        
        else:
            print(f"Brawo! Zgadłeś liczbę {liczba} po {proba} próbach.")
            odpowiedz = input("Czy chcesz zagrać jeszcze raz? (t/n): ")
            if odpowiedz.lower() == "t":
                break
            else:
                print("Dziękuję za grę. Do widzenia!")
                exit()


   
    



