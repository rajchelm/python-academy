import requests

nbp = requests.get("http://api.nbp.pl/api/exchangerates/tables/a").json()
currencies = nbp[0]["rates"]
print("y - Wartość klucza rates - kolejna lista z walutami:", "\n", currencies)
print()

for curr in currencies:
    print()
    for key, value in curr.items():
        print(key + ":", value)
