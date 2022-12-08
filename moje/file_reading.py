with open("numbers.txt", "r") as file:
    numbers = file.readlines()
    total = 0
    for number in numbers:
        total += int(number)

    print(f"sum of balues equals {total}")
