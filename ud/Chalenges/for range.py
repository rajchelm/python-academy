# Zadania z for i range
# 1) Stwórz zmienną sum, która będzie miała ustawioną wartość 0 przed każdą pętlą
# 2) Zrób pętlę for z wartościami od 0 do 200 z range, zsumuj liczby i wyświetl
#    rezultat w konsoli
# 3) Zrób pętlę for z range z liczbami od 50 do 100, dodaj je i wyświetl wynik
# 4) Zrób kolejną pętlę z range od 0 do 300 z krokiem co 3, dodaj liczby
#    i wyświetl wynik w konsoli


sum = 0
for v in range(200):
    sum += v
print(sum)
print()

sum = 0
for v in range(50, 100):
    sum += v
print(sum)
print()

sum = 0
for v in range(0, 300, 3):
    sum += v
print(sum)