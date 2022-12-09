# slownik - nawiasy klamrowe, klucz : wartość

contacts = {
    "Ola" : "ola@example.com",
    "Daniel" : 30,
    "Ania" : "ania@example.com"
}

contacts["Rafał"] = "rafal@example.com"     #dodanie elementu do slownika


print(contacts["Ola"])      # wyświetlenie wartości dla klucza Ola
print(contacts["Daniel"])   # wyświetlenie wartości dla klucza Daniel
print(type(contacts))       # wyświetlenie typu zmiennej (słownik)
print(len(contacts))        # ilość elementów w slowniku

print(contacts.keys())      # wyświetlenie wszystkich kluczy słownika
print(contacts.values())    # wyświetlenie wszystkich wartości słownika

print(" ")                  #odstęp

for key in contacts:
    print(key + " " + str(contacts[key]))   #wyświetlanie kluczy i wartości

print(" ")

for key, value in contacts.items():
    print(key, " ", value)      #wyświetlanie kluczy i wartości
