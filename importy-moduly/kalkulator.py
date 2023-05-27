import modul

while True:
    działanie = input("Wybierz jakie działanie chcesz wykonać ('+','-','*','/','0' - kończy program: ")
    if działanie == '0':
        print("Koniec programu") 
        break
    if działanie not in ['+','-','*','/']:
        print("Nieznana operacja")
        break
    
    a = float(input("Podaj liczbę a: "))
    b = float(input("Podaj liczbę b: "))

    if działanie == '+':
        print(modul.dodawanie(a,b))
        
    elif działanie == '-':
        print(modul.odejmowanie(a,b))
        
    elif działanie == '*':
        print(modul.mnożenie(a,b))
        
    else:
        try:
            print(modul.dzielenie(a, b))
        except ZeroDivisionError:
            print("Błąd: Dzielenie przez zero!")