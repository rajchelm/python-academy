# operatory tożsamości - is, is not
# Porównują lokalizację w pamięci operantów. W przypadku is jeśli operandy wskazują na to samo miejsce
# w pamięci to zwrócone jest True. W przypadku is not na odwrót, zwróci True jesli nie wskazuja na to samo
# miejsce w pamięci.




strData = "test"

print( dir(strData) )               # metoda pokazująca sporo informacji o możliwościach stringa

print( strData.upper() )            # wywołanie jednej z funkcji printa

intData = 10
print( dir(intData) )

a = [1,2,3,4,5]
b = a

print( a is b )                     # sprawdzenie czy a ma to samo miejsce w pamięci co b

a.append(77)                        # dodanie do listy jednego elementu
print(a, b)                         # a i b
print( a is b )

c = [3,4,5]                         # nowa lista
print(a is c)                       # False
print(a is not c)                   # True bo a jest w innym miejscu pamięci niż c


