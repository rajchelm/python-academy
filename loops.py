for i in range(10):
    print(i)

fruits = ["apple", "banana", "error", "grape"]
name = "stefan"

for fruit in fruits:    #drukowanie elementów z listy fruits
    if fruit == "error":
        continue
    print(fruit)

for letter in name:     #drukowanie liter ze stringa name
    if letter in "1234567890":
        print(f"{letter} is not a letter!")
        break
    print(letter)

# a, b = 0, 10    #to samo co a = 0, b = 10
# while a < b:
#     print(f"a={a}, b={b}")
#     a += 1

# a, b = 10, 100
# while a < b:
#     print(a)
#     a +=2

for i in range(10, 100):
    if i % 2 == 0:
        print(i)
#
# for i in range(10, 100, 2):
#     print(i)
#
# a = 10
# while a < 100:
#     print(a)
#     a += 2