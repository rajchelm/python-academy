"""
Scope- zasięg zmiennych - zmienne lokalne
zmienne lokalne zadeklarowane są np wewnątrz funkcji i tylko  tam są dostępne czyli
zmienna zdefiniowana w np funkcji nie będzie widoczna poza nią
instrukcja if, pętle, try, except nie definiują zasięgu - zawsze odwołują się do zmiennej globalnej

Zmienne lokalne o tej samej nazwie co globalne je przesłaniają. Podczas wywołania funkcji gdy potrzebny jest dostęp
do zmiennej Python sprawdza czy przypadkiem o tej samej nazwie nie jest zadeklarowana wewnątrz funkcji, taka
ma pierwszeństwo. Jeśli nie jest zadekl wewn funkcji to zmianna jest szukana stopień wyżej w glonalnych zmiennych.
Jeśli funkcja jest częścią innejn funkcji to zmienna jest poszukiwana zawsze o poziom wyżej jeśli nie ma jej w środku.

Chcąc w funkcji zmienić zmienną globalną trzeba to opisać w funkcji np. "global zmienna" co nie utworzy kolejnej
zmiennej wewnątrz funkcji tylko będzie się zawsze odwoływało do globalnej.
"""

number = 12

def test1():
    print(number)       # 12
test1()     # 12

def test2():
    number = 100
    print(number)       # 100
    if 1 == 1:
        print(number)   # 100
        if 2 == 2:
            number = 50
            print(number)   # 50
    print(number)       # 50
test2()     # 100
print(number)       # 12

print("\n test3")

def test3():            # funkcja z odwołaniem do zmiennej globalnej
    global number
    number = 5
    print("test3", number)      # 5 bo odwołaliśmy number do zmiennej globalnej
    if 1 == 1:
        number = 6
        print("test3", number)      # 6
test3()
print("global number after test3(): ", number)      # 6


print("\n test4")

number = 10
def test4(number):          # zmienna która jest też parametrem
    print("test4 param: ", number)
    number = 20
    print("test4 after change: ", number)
test4(33)
print("global number after test4(): ", number)


print("\n test5")

number = 10
def foo():
    print("foo() number: ", number)     # 10

def bar():
    number = 9
    print("bar() number: ", number)     # 9
    foo()           # 10 bo w definicji foo nie ma zadeklarowanej zmiennej więc szuka wyżej w globalnej
bar()
print("global number after foo(): ", number)


print("\n check1 & check2")
number = 20
def check1():
    number = 12
    print("check1() number: ", number)  # 12
    def check2():
        print("check2 number", number)  # 12
    check2()

check1()
print("global number after check1() :", number)     # 20


print("\n if test")
if 1 == 1:
    data = 100      # utworzy sie zmienna data bo if jest true
print(data)
if 1 == 2:
    nextData = 15   # zmienna nextData nie utworzy sie bo if nie jest true