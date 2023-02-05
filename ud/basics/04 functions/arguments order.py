"""
Ograniczenie sposobu przekazywania danych do funkcji
Za pomocą / oraz * można określić dopuszczalne sposoby przekazywania argumentów do funkcji.
Slash / oznacza parametry tylko pozycyjne, ważna jest kolejność tych parametrów i nie mogą być przekazywane jako argumenty
nazwane. Uwaga - parametry tylko pozycyjne umieszczane są przed / dzięki temu rozdziela parametry tylko pozycyjne
od reszty parametrów.
Gwiazdka * oznacza argumenty nazwane, musi byc umieszczona przed pierwszym parametrem, który ma być tak przekazany

"""

def printData(string, number = 10, /):
    print(string, number)

printData("Test", 5)            # to zadziała prawidłowo bo argumenty są nie nazwane i zgodnie z kolejnością

# printData(string = "test", number = 11)    # ta linie spowoduje błąd bo funkcja zawiera / więc nie definiujemy argumentów nazwanych


def printCar(brand, /, name = "concept", *, year = 1960, color = "black"):
    print(brand, name, year, color)

printCar("Ford", "Mustanc", color="blue", year=1973)








