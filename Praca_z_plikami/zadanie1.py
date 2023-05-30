from os import path
import string


dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path = path.join(dir_path, filename)


with open(data_path, "r", encoding="utf-8") as f:
    tekst = f.read()
    for char in string.punctuation:
        tekst = tekst.replace(char, '')
   
    slowa = len(tekst.split())  
    words = tekst.split()
    print(f'Ilość słów w pliku: {slowa}')
    last_letters = {}

    for word in words:
        last_letter = word[-1]
        if last_letter in last_letters:
            last_letters[last_letter] += 1
        else:
            last_letters[last_letter] = 1

    for letter, count in last_letters.items():
        print(f'Litera {letter} występuje: {count} razy.')
    
   





