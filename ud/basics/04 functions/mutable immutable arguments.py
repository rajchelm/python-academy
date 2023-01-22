"""
        Przekazywnaie wartości do funkcji w postaci parametrów - mutable vs immutable
Definiując funkcję oraz przyjmowane przez nią parametry musimy pamiętać o charaktersytyce typów w Python.
Typy niemutowalne int, float, tuple, str i bool czyli ich zmiana tworzy nowy element w pamięci.
Typy mutowalne przy modyfikacji nie tworzą nowego elementu w pamięci, są zmieniane np set, list, dict
Typ str jest niemutowalny więc zmiana przekazanego łańcucha wewnątrz funkcji spowoduje powstranie nowego łańcucha,
oryginalny bedzie bez zmian.
"""

f = 3.2         # niemutowalne: int, float, bool, str, frozenset
addr1 = id(f)

f = f + 2.5
addr2 = id(f)

print(addr1)
print(addr2)
print(addr1 == addr2)


listData = ["a", "b"]       # mutowalne list set dict
addr1 = id(listData)
listData += ["c", "d"]
addr2 = id(listData)

print(addr1)
print(addr2)
print(addr1 == addr2)


"""
przykład ze stringiem - niemutowalny typ
Takie rozwiązanie powoduje utworzenie w pamięci nowego łańcucha z wykrzykniniem, który nie jest zwracany.
więc to nie najlepsze rozwiązanie. Z czasem Garbage Collector usunie nieużywaną wartość z pamięci
"""

def addToStr(string):
    string += "!"
    print("addToStr() string jako:" + string)
string = "Hello"

addToStr(string)
addToStr(string)
addToStr(string)
print("oryginalny: " + string)


"""
Lista jest mutowalna więc wszelkieoperacje na niej w funkcji nie tworzą nowej listy tylko ją modyfikują.
Funkcja addToList dodaje element do listy, może go zmodyfikować ponieważ listy są mutowalne.
Podobnie będzie w przypadku set oraz dict czyli zbiorów (oprócz frozenset) i słowników
"""

def addToList(someList):
    someList.append(4)

listData = [2]
addToList(listData)
addToList(listData)
addToList(listData)

print("ostateczna lista: " + str(listData))

"""
Funkcja addToLiest przypisuje nową listę do someList czyli nie wskazuje już na przekazaną listę w parametrze.
Oryginalna lista w listData nie jest zmodyfikowana ponieważ zmienna ta nadal wskazuje na początkową listę.
someList przed zmianą: [2]
someList po zmianie: [30, 40, 50]
ostateczna lista: [2]
"""
def addToList(somelist):
    print("someList przed zmianą: " + str(somelist))
    someList = [30,40,50]
    print("someList po zmianie: " + str(someList))

listData = [2]
#przypisanie nowej listy w funkcji nie zmienia listData
addToList(listData)
print("ostateczna lista: " + str(listData))