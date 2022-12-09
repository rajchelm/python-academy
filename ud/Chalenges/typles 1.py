# 1. Stwórz krotkę z wartościami: 50, 100, 150, 200, 250
# 2. Pokaż typ krotki w konsoli
# 3. Pokaż w konsoli ilość elementów krotki
# 4. Pokaż ostatni element krotki wykorzystując len() -1
# 5. Następnie pokaż elementy od drugiego do czwartego
# 6. Pokaż trzeci element od końca z ujemnym indeksem


krotka = 50, 100, 150, 200, 250

print(type(krotka))
print(len(krotka))
print(krotka[len(krotka)-1])
print(krotka[1:4])
print(krotka[-3])