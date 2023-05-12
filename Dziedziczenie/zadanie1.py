from abc import ABC


class Figura(ABC):
    def __init__(self, nazwa):
        self._nazwa = nazwa
    
    
    def oblicz_pole(self):
        pass
    
    
    def oblicz_obwod(self):
        pass

    def get_nazwa(self):
        return self._nazwa


class Prostokat(Figura):
    def __init__(self, nazwa, bok_a, bok_b):
        super().__init__(nazwa)
        self._bok_a = bok_a
        self._bok_b = bok_b
    
    def oblicz_pole(self):
        return self._bok_a * self._bok_b
    
    def oblicz_obwod(self):
        return 2 * (self._bok_a + self._bok_b)

class Kwadrat(Figura):
    def __init__(self, nazwa, bok_aa):
        super().__init__(nazwa)
        self._bok_aa = bok_aa
        
    
    def oblicz_pole(self):
        return self._bok_aa * self._bok_aa
    
    def oblicz_obwod(self):
        return 4 * (self._bok_aa)

class Trojkat(Figura):
    def __init__(self, nazwa, podstawa, wysokosc):
        super().__init__(nazwa)
        self._podstawa = podstawa
        self._wysokosc = wysokosc
    
    def oblicz_pole(self):
        return 0.5 * self._podstawa * self._wysokosc
    
    def oblicz_obwod(self):
        return "Nie da się obliczyć obwodu dla tego trójkąta."





figury = [Prostokat("Prostokąt 1", 5, 10),Kwadrat("Kwadrat 1", 6), Trojkat("Trójkąt 1", 4, 6)]
for figura in figury:
    print(f"{figura.get_nazwa()}: pole = {figura.oblicz_pole()}, obwód = {figura.oblicz_obwod()}")

