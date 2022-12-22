import requests

nbp = requests.get("http://api.nbp.pl/api/exchangerates/tables/a").json()

x = nbp[0]
print("x - wartość pierwszego elementu otrzymanej listy:", x)
print()

y = x["rates"]
print("y - Wartość klucza rates - kolejna lista z walutami:", y)

print()
for curr in y:

    print()
    for key, value in curr.items():
        print(key + ":", value)
