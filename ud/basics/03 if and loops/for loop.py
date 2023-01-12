"""
for - pętla
for słuzy do iterownaia sekwencji listy, krotki, słownika, zbioru czy łańcucha znaków
"""

listData = [1,2,3,4]            # iteracja listy
for v in listData:
    print(v)


tupleData = ("one", "two", "three")     # iteracja krotki
for v in tupleData:
    print(v)


setData = {3,2,1}               # iteracja zbioru
for v in setData:
    print(v)


strData = "Hello"               # iteracja stringa
for v in strData:
    print(v)

                                #
                                # iteracja słownika
dictData = {"Ola":"ola@example.com", "Ania":"ania@example.com"}
for v in dictData:
    print(v)                # wyświetlanie samych kluczy słownika

for v in dictData:
    print(dictData[v])      # wyświetlenie samych wartości słownika

for key, value in dictData.items():
    print(key, " : ", value)    # wyświetlenie klucza i wartości

for key in dictData.keys():
    print(key)              # alternatywne wyświetlanie samych kluczy słownika

for value in dictData.values():
    print(value)            # alternatywne wyświetlanie samych kluczy słownika


                    ####### for z else - else wykona instrukcję po zakończeniu fora
for value in dictData.values():
    print(value)
else:
    print("pętla for zakończona")