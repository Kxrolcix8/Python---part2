slowo = str(input("Podaj dowolne słowo i sprawdź czy jest palindromem: ")) 
  
o_slowo = slowo[::-1]

if (slowo == o_slowo):
    print("To palindrom")
else:
    print("To nie palindrom")