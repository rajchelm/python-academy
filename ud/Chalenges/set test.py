# 1. Stwórz set z unikalnymi wartościami jak:
#    Ania, Kasia, Ola, Karol, Daniel, Zuza
# 2. Dodaj do set za pomocą funkcji add kolejne elementy:
#    Olek, Basia, Kasia, Karol, Zuza, Paulina
# 3. Pokaż w konsoli wielkosc set
# 4. Wykorzystaj pętlę for aby pokazać elementy w set

mySet = {"Ania", "Kasia", "Ola", "Karol", "Daniel", "Zuza"}
mySet.add("Olek")
mySet.add("Basia")
mySet.add("Kasia")
mySet.add("Karol")
mySet.add("Zuza")
mySet.add("Paulina")

print("Wielkość zbioru:", len(mySet))

for s in mySet:
    print(s)