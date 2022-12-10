setData = {2, 3, 1, 4 ,5}   # sety - nieuporządkowane zbiory unikalnych wartości
setData.add(22)             # dodanie do seta nowej wartości 22
setData.discard(1)          # usunięcie elementuz wartością 1 ze zbioru
print(setData)
print(type(setData))

for v in setData:
    print(v)                # wyświetlenie wszystkich elementów zbioru w nowych liniach


frozenData = frozenset(setData) # konwersja naszego zbioru na zbiór niemutowalny - nie mozna go edytować
print(type(frozenData))

for value in frozenData:
    print(value)