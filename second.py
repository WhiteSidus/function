def objem(radius):
    if radius > 0:
        vysledek = (4/3)*(3.14*radius**3) 
        return vysledek
    else: 
        print("Mate chybu!")

radius = int(input("Zadejte radius koule: "))

print("Výsledek je: ", objem(radius))
