pesel = "55030101193"
weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

length = len(weights) #zwraca d lugość listy

sum =0
for i in range(length):
    sum += int(pesel[i]) * weights[i]
print(sum)
checksum = 10 - sum % 10
print(checksum)
