# mypy do pobrania 
def dodawanie (a: int ,b:int):
    """Wykonuje dodawanie: """  
    return a+b
def odejmowanie (a: int ,b:int):
    """Wykonuje odejmowanie: """
    return a-b
def mnożenie (a: int ,b:int):
    """Wykonuje mnożenienie: """
    return a*b
def dzielenie (a: int ,b:int):
    """Wykonuje dzielenie: """
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
       
       print(dodawanie.__doc__)
       print(dodawanie(a,b))
        
    elif działanie == '-':
        print(odejmowanie.__doc__)
        print(odejmowanie(a,b))
        
    elif działanie == '*':
        print(mnożenie.__doc__)
        print(mnożenie(a,b))
        
    else:
        print(dzielenie.__doc__)
        print(dzielenie(a,b))
        
     





