import random

while True:
    los = random.randint(0, 100)
    proba = 0

    try:
        liczba = int(input("Podaj i zgadnij wylosowaną liczbę: "))
        print(los)
    except ValueError:
                print("To nie jest liczba. Spróbuj ponownie.")
                continue

    while True:
        try:
            if los < liczba:
                print("Wylosowana liczba jest mniejsza")
                proba += 1
                liczba = int(input("Podaj inną liczbę: "))
            elif los > liczba:
                print("Wylosowana liczba jest większa")
                proba += 1
                liczba = int(input("Podaj inną liczbę:  "))
            else:
                print(f"Brawo! Zgadłeś liczbę {liczba} po {proba} próbach.")

                odpowiedz = input("Czy chcesz zagrać jeszcze raz? (t/n): ")
                if odpowiedz.lower() == "t":
                    break
                else:
                    print("Dziękuję za grę. Do widzenia!")
                    exit()
        except ValueError:
                print("To nie jest liczba. Spróbuj ponownie.")
                continue



