destination = "Gdansk"
destinations_dict = {
    "Nicosia": 2000,
    "Reykjavik": 2900,
    "Chartum": None,
    "Gdansk": 1000
}

distance = destinations_dict[destination]

if distance:
    if distance >=2000:
        cost = distance * 2
    else:
        cost = distance * 2 + 100   #equivalent to cost
    print(f"total cost to {destination} is {cost}")
else:
    print(f"there is no destination {destination}")



"""
a = 18
if a > 0:
    print("Value is positive")
elif a==0:
    print("Value is 0")
else:
    print("Value is negative")
"""