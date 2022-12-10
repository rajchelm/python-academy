# Typ None oznacza brak wartości np, że zmienna nie posiada przypisanej wartosci

data = None
print(type(data))       # Typ None

if data is True:
    print("Data is true")
elif data is False:
    print("Data is False")
else:
    print("None is None")


currentTaskNumber = 10
currentTaskNumber = None
currentTaskNumber = 14
