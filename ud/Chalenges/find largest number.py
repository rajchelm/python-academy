# 1. Napisz funkcję findLargest która przyjmuje dwie liczby jako parametry num1 i num2.
#    Funkcja musi pokazać w konsoli informację, która liczba jest większa oraz jej wartość.
#    np: "num1 jest większą liczbą: 12" lub, że obie liczby są równe.
#    Pamiętaj aby użyć if elif oraz else.
# 2. Dodatkowo funkcja zwraca większą liczbę dzięki return
# 3. Sprawdź funkcję przekazując wartości 3 i 10, pokaż w konsoli zwróconą wartość z funkcji
# 4. W ten sam sposób sprawdź funkcję dla 12 i 7


def findLargest(num1, num2):
    if num1 > num2:
        larger = num1
        print("num1 jest większą liczbą:", larger)
    elif num2 > num1:
        larger = num2
        print("num2 jest większa liczbą:", larger)
    else:
        print("num1 jest równe num2:", larger,"=", larger)
        larger = "liczby są równe"
    return larger
print(findLargest(1,2))