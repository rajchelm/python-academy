# Konwersja na bool - puste dane dają zawsze False
# tzw FALSY VALUES

print(bool())           # Brak przekazanej wartości zwróci False
print(bool(False))      # False
print(bool(0))          # wartość int 0  to False
print(bool(0.0))        # wartość float 0 to False
print(bool(()))         # puste krotki to False
print(bool([]))         # puste listy to False
print(bool({}))         # puste zbiory to False
print(bool(""))         # pusty string to False
print(bool(None))       # None to brak wartości wiec też False

print(bool(True))       # True
print(bool(-5))         # jakakolwiek wartość nawet ujemna to True
print(bool((6, 1)))   # krotka z przynajmniej jednym elementem to True
print(bool([0]))        # Lista z przynajmniej jednym elementem to True
print(bool({0}))        # zbiór z przynajmniej jednym elementem to True
print(bool(" "))        # string z przynajmniej jednym elementem to True