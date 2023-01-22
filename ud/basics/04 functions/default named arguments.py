"""
Funkcje mogą być wywyłane przy uzyciu argumentów nazwanych, dzięki czemu nie jest wymagana odpowiednia kolejność
przekazywania danych do funkcji.
Argument nazwany przekazujemy jako parę: argument = wartość
Argumenty nazwane mogą być przesyłane w dowolnej kolejności
"""

def showData(string, number):
    print(string, str(number))

showData(string = "Liczba: ", number = 10)
showData(number = 10, string = "Liczba: ")

def printUser(name, country = "unknown", email = "default@mail.com"):
    print("User: ", name, "from country:", country, "and email:", email)

printUser(country="UK", name="Ania")