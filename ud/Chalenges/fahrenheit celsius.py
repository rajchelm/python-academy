# Napisz dwie funkcje konwertujące temperaturę:
# 1) Funkcja cToF skonwertuje stopnie Celsjusza na Fahrenheita z wzoru:
#    fahrenheit = celsius * 9 / 5 + 32
# 2) Funkcja fToC konwertuje stopnie Fahrenheita na Celsjusza z wzoru:
#    celsius = (fahrenheit - 32) * 5 / 9;
# 3) Dodatkowo w konsoli pokaż wynik konwersji np:
#    "20 stopni Celsjusza to 68 stopni Fahrenheita" itd.
#    Jeśli chcesz użyj w string specjalnego znaku stopni ° za pomocą \xB0
# 4) Skonwertuj 20°C na Fahrenheita (68°F)
#    Skonwertuj 86°F na Celsjusza (30°C)


def cToF(celsius):
    return celsius * 9 / 5 + 32

def fToC(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

tempCel = input("Podaj temperaturę w stopniach Celsiusa: ")
print(f"{tempCel}\xB0C to {cToF(int(tempCel))}\xB0F")

tempFahr = input("\nPodaj temperaturę w stopniach Fahrenheit: ")
print(f"{tempFahr}\xB0F to {fToC(int(tempFahr))}\xB0C")

