def dodawanie (a ,b):
    return a+b
def odejmowanie (a ,b):
    return a-b
def mnożenie (a ,b):
    return a*b
def dzielenie (a ,b):
    if b == 0:
        raise ValueError("Nie można dzielić przez 0!")
    return a/b

while True:
    try:
        działanie = input("Wybierz jakie działanie chcesz wykonać ('+','-','*','/','0' - kończy program: ")
        if działanie == '0':
            print("Koniec programu") 
            break
        if działanie not in ['+','-','*','/']:
            print("Nieznana operacja")
            continue
        
        a = float(input("Podaj liczbę a: "))
        b = float(input("Podaj liczbę b: "))

        if działanie == '+':
            print(dodawanie(a,b))
            
        elif działanie == '-':
            print(odejmowanie(a,b))
            
        elif działanie == '*':
            print(mnożenie(a,b))
            
        else:
            print(dzielenie(a,b))

    except ValueError as e:
        print("Niepoprawny format danych", e)
        
     





