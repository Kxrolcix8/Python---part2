import random
from typing import Set



with open('imiona.txt', 'r', encoding='utf-8') as f:
    imiona = f.read().splitlines()


with open('nazwiska.txt', 'r', encoding='utf-8') as f:
    nazwiska = f.read().splitlines()


liczba_kombinacji = int(input("Podaj liczbę kombinacji imion i nazwisk do wygenerowania: "))


kombinacje: Set[str] = set()
while len(kombinacje) < liczba_kombinacji:
    imie = random.choice(imiona)
    nazwisko = random.choice(nazwiska)
    kombinacja = f"{imie} {nazwisko}"
    kombinacje.add(kombinacja)

with open('kombinacje.txt', 'w') as f:
    for i in kombinacje:
        f.write(f"{i}\n")
