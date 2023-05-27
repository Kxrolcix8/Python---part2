krotka = (10, -3, 4, 9, 12, -6, 0)

min = None
max = None
for i in krotka: 
    if min == None or min > i: 
        min = i       
    if max == None or max < i:
        max = i        
print ("najmniejsza liczba to:", min)
print ("największa liczba to:", max)