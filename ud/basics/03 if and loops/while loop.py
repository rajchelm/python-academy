"""
while - pętla
Pętla while wykonuje sie tak długo jak warunek jest spełniony czyli zwraca true. Gdy warunek już nie jest spełniony
to kontrola pragramu przechodzi do kolejnej instrukcji

"""

number = 4
while number > 0:
    print(number)
    number -= 1
print("koniec pierwszego while")
number = 0
while number <6:
    print(number)
    number += 1
print("koniec pierwszego while")

# num = 0
# while True:             # Pętla nieskończona
#     print("Wprowadź liczbę lub wpisz exit aby zakończyć")
#     strData = input()
#     if strData == "exit" : break
#     num += int(strData)
#     print("Wartość po dodaniu liczby: ", str(num))
# print("kod po petli")


number = 4
while number > 0:
    print(number)
    number -= 1
else:
    print("number po pętli: ", str(number))