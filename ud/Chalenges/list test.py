data = [0, 1, 2, 3, 4, 5, 6]

print("długość listy: ",len(data))
del data[1]
print("długość listy po skasowaniu elementu: ",len(data))

if 3 in data:
    print("3 jest w liście")

for el in data:
    print("Element z listy: ", el)

for el in data:
    print("element z listy z dodaną wartością 2: ", el + 2)

for el in data:
    print("element z listy z wartością * 2: ", el * 2)