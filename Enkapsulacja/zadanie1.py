class Czytelnik:
    id: int = -1


    def __init__(self, imie: str, nazwisko: str, kierunek: str):
            Czytelnik.id += 1
            self.__id = Czytelnik.id
            self.__czytelnik = self.stworz_czytelnika(imie, nazwisko)
            self.__kierunek = kierunek
    

    def stworz_czytelnika(self,imie: str, nazwisko: str) -> dict:
        return{"imie":imie, "nazwisko":nazwisko}

    def pobierz_kierunek(self) -> str:
        return self.__kierunek
    def pobierz_id(self) -> int:
        return self.__id


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


print(czytelnik1.pobierz_kierunek())
print(czytelnik1.pobierz_id())








        
