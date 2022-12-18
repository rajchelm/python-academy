import requests

# res = requests.get("https://api.punkapi.com/v2/beers?brewed_before=01-2011&brewed_after=12-2009")
# beers_list = res.json()
# status_code = res.status_code
# raw_status_code = res.text
# print(res)

res = requests.get("https://api.ipify.org/?format=json")
print(res)