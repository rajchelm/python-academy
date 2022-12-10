floatNum = 23.99234234          # zmienna z typem float
intNum = int(floatNum)          # konwersja zmiennej z wartością float na int - ułamek jest obcięty
print(intNum)
print(type(intNum))

print(int("  678    "))         #jesli w stringu występują cyfry to również można go zamienić na int

intNum = 56
float1 = float(intNum)
print(type(float1))
print(float1)


print("wartość float1: ", str(float1))