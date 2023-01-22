"""
            Domyślne wartości argumentów funkcji
Python pozwala na podanie domyślnej wartości jednego lub wielu arguemtnów funkcji. Taką funkcję można wywołać z mniejszą
ilością argumentów niż te w definicji funkcji, ich wartości będą domyślne wewnątrz funkcji.
Pierwszy argument poniższej funkcji nie jest domyślnym, więc musi być zawsze podany.
"""
def printUser(name, country = "unknown", email = "default@mail.com"):
    print("User: ", name, "from country:", country, "and email:", email)

printUser("Jasiek")
print()
printUser("Adam", "Poland", "adam@mail.com")
printUser("zbyszek", "katar")