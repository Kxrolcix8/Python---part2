wiek = int(input("Ile masz lat?"))
pj = True if input("Czy maz prawo jazdy kat.A2? (t/n): ")  \
    in ("t","ta", "tak", "T") else False
lata = 0
if pj:
    lata = int(input("Ile lat masz prawo jazdy kat.A2? "))

if wiek >= 24 or (pj and wiek >= 20 and lata >= 2):
    print("Możesz robić prawo jazdy A")
else:
    print("Nie możesz robić prawo jazdy A")




