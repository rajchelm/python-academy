#                           Program kalkulator w konsoli

num = 0
operation = None        # wartość początkowa nie jest zdefiniowana
reset = True
result = None
calcOperations = ["+", "-", "*", "/", "**"]

while True:
    if reset == True:
        num = int( input("podaj liczbę startową: "))      # do inputa można wpisać text wyświetlany w konsoli przed odczytem
        reset = False

    operation = input("Podaj operację arytmetyczną z dostępnych: " + str(calcOperations) + " lub wpisz exit jeśli koniec lub reset: ")
    if operation == "exit": break
    if operation == "reset":
        reset = True
        continue
    if not operation in calcOperations:
        print("Wprowadzona została błędna operacja")
        continue

    secondnum = int(input("Podaj drugą liczbe: "))

    if operation == "+":
        result = num + secondnum
    if operation == "-":
        result = num - secondnum
    if operation == "*":
        result = num * secondnum
    if operation == "/":
        result = num / secondnum
    if operation == "**":
        result = num ** secondnum

    print("Wynik operacji ", str(num), str(operation), str(secondnum), " = ", str(result))

    num = result
    result = None