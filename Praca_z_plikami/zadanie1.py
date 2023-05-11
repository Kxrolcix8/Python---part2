from os import path

nwords = 0
dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path = path.join(dir_path, filename)


with open(data_path, "r", encoding="utf-8") as file:
    
    for line in file:
        
        words = line.split()
        nwords += len(words)
print("Liczba słów łącznie: " + str(nwords))





