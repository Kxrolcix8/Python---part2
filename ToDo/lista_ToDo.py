import json
from datetime import datetime


zadania = []


try:
    with open('tasks.json', 'r') as file:
        zadania = json.load(file)
except FileNotFoundError:
    print("Nie znaleziono pliku. Tworzę nowy plik z zadaniami.")


def dodaj_zadanie():
    if zadania:
        max_id = max(zadania, key=lambda x: x['id'])['id']
        ID = max_id + 1
    else:
        ID = 1
    tytul = input("Podaj tytuł zadania: ")
    opis = input("Podaj opis zadania: ")
   
    while True:
        data_str = input("Podaj termin wykonania zadania (DD-MM-YYYY): ")
        try:
            data = datetime.strptime(data_str, "%d-%m-%Y")
            if data < datetime.now():
                print("Podana data jest przeszła. Podaj przyszłą datę.")
            else:
                break
        except ValueError:
            print("Nieprawidłowy format daty. Podaj datę w formacie DD-MM-YYYY.")
            continue
    zadanie = {'id': ID, 'title': tytul, 'description': opis, 'due_date': data}
    zadania.append(zadanie)
    print(f"Dodano zadanie: {tytul}")


def usun_zadanie():
    zad_id = int(input("Podaj id zadania do usunięcia: "))
    for zadanie in zadania:
        if zadanie['id'] == zad_id:
            zadania.remove(zadanie)
            print(f"Usunięto zadanie o id: {zad_id}")
            return
    print(f"Nie znaleziono zadania o id: {zad_id}")


def aktualizuj_zad():
    zad_id = int(input("Podaj id zadania do aktualizacji: "))
    for zadanie in zadania:
        if zadanie['id'] == zad_id:
            tytul = input("Podaj nowy tytuł zadania: ")
            opis = input("Podaj nowy opis zadania: ")
            data = input("Podaj nowy termin wykonania zadania (DD-MM-YYYY): ")
            zadanie['tytul'] = tytul
            zadanie['opis'] = opis
            zadanie['data'] = data
            print(f"Aktualizowano zadanie o id: {zad_id}")
            return
    print(f"Nie znaleziono zadania o id: {zad_id}")


def wyswietl_zad():
    if zadania:
        for zadanie in zadania:
            print(f"id: {zadanie['id']}, tytuł: {zadanie['tytul']}, termin wykonania: {zadanie['data']}")
            pokaz_opis = input("Czy wyświetlić opis zadania? (T/N): ")
            if pokaz_opis.lower() == "t":
                print(f"Opis zadania: {zadanie['opis']}")
    else:
        print("Brak zapisanych zadań.")


def zapisz_zad():
    with open('tasks.json', 'w') as file:
        json.dump(zadania, file)
    print("Zapisano zadania do pliku.")


while True:
    print("""
    Twoja Lista ToDO!
    Wybierz jedną z opcji:
    1. Dodaj zadanie
    2. Usuń zadanie
    3. Aktualizuj zadanie
    4. Wyświetl zadania
    5. Zapisz zadania do pliku
    6. Wyjdź z programu
    """)
    choice = input("Twój wybór: ")
    if choice == "1":
        dodaj_zadanie()  
    elif choice == "2":
        usun_zadanie()
    elif choice == "3":
        aktualizuj_zad()
    elif choice == "4":
        wyswietl_zad()
    elif choice == "5":
        zapisz_zad()
    elif choice == "6":
        zapisz_zad()
        print("Koniec programu.")
        break
    else:
        print("Nieprawidłowy wybór. Wybierz opcję od 1 do 6.")


