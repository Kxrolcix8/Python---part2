from abc import ABC, abstractmethod

#tworzenie klas ,w tym abstrakcyjnych
class Figura(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def oblicz_pole(self):
        pass
    
    @abstractmethod
    def oblicz_obwod(self):
        pass



class Prostokat(Figura):
    def __init__(self,bok_a, bok_b):
        super().__init__()
        self._bok_a = bok_a
        self._bok_b = bok_b
    
    def oblicz_pole(self):
        return self._bok_a * self._bok_b
    
    def oblicz_obwod(self):
        return 2 * (self._bok_a + self._bok_b)

class Kwadrat(Figura):
    def __init__(self, bok_aa):
        super().__init__()
        self._bok_aa = bok_aa
        
    
    def oblicz_pole(self):
        return self._bok_aa * self._bok_aa
    
    def oblicz_obwod(self):
        return 4 * (self._bok_aa)

class Trojkat(Figura):
    def __init__(self, podstawa, wysokosc):
        super().__init__()
        self._podstawa = podstawa
        self._wysokosc = wysokosc
    
    def oblicz_pole(self):
        return 0.5 * self._podstawa * self._wysokosc
    
    def oblicz_obwod(self):
        return "Nie da się obliczyć obwodu dla tego trójkąta."

#definiowanie obiaktów

prostokat1 = Prostokat(2,6)
prostokat2 = Prostokat(6,10)
kwadrat = Kwadrat(5)
trojkat = Trojkat(3,6)

#printowanie funkcji
print("Prostokąt 1, Pole: ")
print(prostokat1.oblicz_pole())
print("Obwód: ")
print(prostokat1.oblicz_obwod())

print("Prostokąt 2, Pole: ")
print(prostokat2.oblicz_pole())
print("Obwód: ")
print(prostokat2.oblicz_obwod())

print("Kwadrat, Pole: ")
print(kwadrat.oblicz_pole())
print("Obwód: ")
print(kwadrat.oblicz_obwod())

print("Trójkąt, Pole: ")
print(trojkat.oblicz_pole())
print("Obwód: ")
print(trojkat.oblicz_obwod())


