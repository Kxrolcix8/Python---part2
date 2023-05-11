class Czytelnik:
    id: int = -1


    def __init__(self,
                imie: str, nazwisko: str, kierunek: str):
            Czytelnik.id += 1

            self.id = Czytelnik.id
            self.czytelnik = self.stworz_czytelnika(imie, nazwisko)
            self.kierunek = kierunek
    

    def stworz_czytelnika(self,imie: str, nazwisko: str) -> dict[str,str]:
        return{"imie":imie, "nazwisko":nazwisko}


czytelnik1 = Czytelnik(
    imie = "Anna",
    nazwisko = "Grom",
    kierunek = "Informatyka w Biznesie"
)
czytelnik2 = Czytelnik(
    imie = "Andrzej",
    nazwisko = "Grom",
    kierunek = "Lingwistyka Angielska"
)

print(czytelnik1.id)
print(czytelnik1.czytelnik["imie"])
print(czytelnik1.czytelnik["nazwisko"])
print(czytelnik1.kierunek)

print(czytelnik2.id)
print(czytelnik2.czytelnik["imie"])
print(czytelnik2.czytelnik["nazwisko"])
print(czytelnik2.kierunek)

        
