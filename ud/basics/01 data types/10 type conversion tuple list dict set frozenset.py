listData = [1, 2, 3, 4, 5, 6, 7]     # lista
tupleData = tuple(listData) # z listy na krotkę

tuple2 = ("Ola", "Adam")    # krotka
newList = list(tuple2)      # z krotki na liste

print(listData)
print(tupleData)
print(tuple2)
print(newList)

setData = set(listData)     # lista na set (nieuporządkowany zbiór unikalnych wartosci)
print(setData)

frozensetData = frozenset(listData)     #lista na frozenset
print(frozensetData)

tupleData1 = (("Adam", "adam@example.com"), ("Ola", "ola@example.com"))
dictData = dict(tupleData1)     # krotka na słownik - słownik to klucz i wartośc więc w takiej formie będą zapisane wartości
print(tupleData1)
print(dictData)
print(dictData["Ola"])      #wyświetli wartość dla klucza Ola po konwersji z krotki

