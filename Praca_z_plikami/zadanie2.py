import random
from os import path

filename1 = 'imiona.txt'
dir_path = path.dirname(__file__)
data_path1 = path.join(dir_path, filename1)

with open(data_path1, 'r', encoding='utf-8') as f:
    names = f.read().splitlines()

filename2 = 'nazwiska.txt'
data_path2 = path.join(dir_path, filename2)
with open(data_path2, 'r', encoding='utf-8') as f:
    surnames = f.read().splitlines()

liczba_kombinacji = int(input("Podaj liczbę kombinacji imion i nazwisk do wygenerowania: "))

kombinacje = set()
while len(kombinacje) < liczba_kombinacji:
    name = random.choice(names)
    surname = random.choice(surnames)
    kombinacja = f"{name} {surname}"
    kombinacje.add(kombinacja)

with open('kombinacje.txt', 'w', encoding='utf-8') as f:
    for i in kombinacje:
        f.write(f"{i}\n")

print(f"Stworzone kombinacje: {kombinacje}")
print(f"Liczba {liczba_kombinacji} kombinacji zostało wygenerowanych i zapisanych do pliku 'kombinacje.txt'.")

