def dodawanie (a ,b):
    return a+b
def odejmowanie (a ,b):
    return a-b
def mnożenie (a ,b):
    return a*b
def dzielenie (a ,b):
    return a/b

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
        print(dodawanie(a,b))
        
    elif działanie == '-':
        print(odejmowanie(a,b))
        
    elif działanie == '*':
        print(mnożenie(a,b))
        
    else:
        print(dzielenie(a,b))
        
     





