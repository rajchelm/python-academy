import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/a")#.json()
if response.ok:
        print(response)
        print(response.ok)
        data = response.json()
        # rates = data["rates"]
        # base = data["table"]
        # date = data["effectiveDate"]
        # print("base: " + base)
        # print("date: " + date)
print(data)