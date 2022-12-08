list = ["Ola", "Ania", 23, 99, "Rafał"]     # lista
print(type(list))                           #wyświetlanie typu zmiennej (lista)

print(list[0])      # wyświetlanie 1 elementu z listy
print(list[3])      # wyświetlanie 4 elementu z listy
print(len(list))    # wyświetlanie długości (ilości elementów) listy
print(list[len(list)-1])    # ostatni element z listy
print(list[-1])     # to samo co powyżej - z minusem jest liczone od końca
print(list[1:4])    # elementy od 2 do 3 (0 to pierwszy element ale bez ostatniego czyli 4)
print(list[3:])     # elementy od 4 do końca
print(list[::2])    # wyświetlanie co 2 element zaczyna zawsze od 1

list[0] = "zmiana"  #zmiana elementu 1 z listy
del list[2]         # kasowanie 3 elementu z listy
list.append(999)    # dodawanie do listy na ostatnią pozycję

print(99 in list)   # zwraca True/False jeśli element znajduje sie w liście
print(98 in list)   # jw

if "Ania" in list:
    print("Ania jest w liście list")

for v in list:      # wyświetlanie kazdego elementu z listy w nowych liniach
    print(v)


data = [
    ["Daniel", "Rafał,"],
    ["Kasia", "Ania"],
    ["Ola", "Adam"]
 ]                  # to jest lista wielopoziomowa
print(len(data))    # długość to 3 bo data ma 3 elementy - 3 listy
print(data[0][0])   # Daniel - 1 element z 1 listy
print(data[2][1])   # Adam - 2 element z 3 listy

data1 = [1, 2, 3]
data2 = [4, 5, 6]
numbers = data1 + data2 # sumowanie list
numbersX2 = numbers * 3 # mnożenie listy
print(numbers)
print(numbersX2)