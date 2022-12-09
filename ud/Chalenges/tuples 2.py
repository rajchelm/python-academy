# 1. Stwórz krotkę z ostantnimi wydatkami na koncie
#    bankowym z wartościami: 100, 200, 300, 400, 500, 600
# 2. Policz wydatki z pomocą pętli for i wyświetl w konsoli
#    ostateczną kwotę. Pamiętaj aby stworzyć zmienną
#    z wartością początkową 0 do której dodasz kolejny wydatek

bank = 100, 200, 300, 400, 500, 600
num = 0

for kwota in bank:
    num = num + kwota

print("Suma wydatków: ", num)