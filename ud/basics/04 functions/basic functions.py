"""
                    Definiowanie funkcji
Funkcja to blok kodu który może być wielokrotnie wywołany aby wykonać określoną akcję. Funkcje są podstawą programowania
w każdym języku, gdyż udostępniają wiele gotowych rozwiązań np print() do wyświetlenia informacji w terminalu.
Funkcję definiuje się słowem kluczowym "def" po którym następuje nazwa funkcji oraz nawiasy okrągłe wewnątrz których
mogą być parametry przekazane do funkcji zdefioniowane po przecinku. Nazwy tch zmiennych mogą być dowolne,
ale zgodne z wymaganiami pythona. Blok kodu funkcji rozpoczyna się dwukropkiem, wymaga równiez wcięcia.
Funkcja może zwrócić wartość za pomocą słowa kluczowego "return"
Wywołanie funkcji wykonuje się za pomocą jej nazwy oraz nawiasów okrągłych, przekazujemy również wewnątrz
nawiasów listę parametrów
"""

a = 2
b = 4
def addNumbers(num1, num2):
    result = num1 + num2
    return result

# Funkcja moze być użyta poprzez dodatkową zmienną:
c = addNumbers(a, b)
print(c)

# albo w innej funkcji np print
print(addNumbers(1, b))

# można też skrócić nie używając zmiennej:
def addNum(a,b):
    return a + b

def subNum(num1, num2):
    result = num1 - num2
    return result

value1 = addNum(10, 5)                  # 15
value2 = subNum(value1, 9)              # 6
print(value1)                           # 15
print(value2)                           # 6
print(subNum(100, addNum(12, 18)))      # 70

        # funkcja może mieć dowolną liczbę argumentów
def add4Numbers(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4
print(add4Numbers(1, 2, 3, 4))


                    # Suma koszyka zakupów
def calcBasketValue(basketList):
    basketSum = 0
    for key in basketList:
        basketSum +=basketList[key]
    return basketSum

shoppingBasket = {
    "smartphone" : 1200,
    "TV" : 1500,
    "console" : 1500
}
print("Suma wartości ze zbioru: ", calcBasketValue(shoppingBasket))
