l = ["burak","cukinia","pomidor","cytryna" ,"ananas", "paptyka", "dynia"]
litera = input("Podaj litere: ")
for element in l:
    if element.startswith(litera):
        print(element, end=" ")