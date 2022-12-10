
# niemutowalne typy: int, float, bool, str, tuple, frozenset
# jakakolwiek operacja na tych typach zmienia jego adres w pamięci - zmienia się "id"

a = 1
addr1 = id(a)           # id zmiennej w pamięci

a += 1
addr2 = id(a)

print(addr1)
print(addr2)
print(addr1 == addr2)   # porównanie czy zmienne sa równe -  wynik to True albo False


# typy mutowalne: list, set, dict
# można je edytować więc są na stałe przypisane w pamięci i po zmianie id pozostaje ten sam

listData = [0,1,2]
addr1 = id(listData)

listData += [3,4,5]
addr2 = id(listData)

print(addr1)
print(addr2)
print(addr1 == addr2)

