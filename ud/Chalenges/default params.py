# Funkcja z domyślnymi wartościami parametrów
# 1) Napisz funkcję z parametrami:
#    - email
#    - country z domyślną wartością "Polska"
#    - company z domyślną wartością "Example Ltd"
# 2) Zwróć z funkcji słownik z elementami jak parametry
# 3) Przetestuj funkcję z jednym argumentem ola@example.com
#    oraz drugi przypadek z kasia@example.com będąca z UK

def dictList(email, country = "Polska", company = "Example Ltd"):
    return {"email": email, "country": country, "company": company}

print(dictList("ola@example.com"))
print(dictList("kasia@example.com", country = "UK"))
print(dictList("adam@example.com", company = "Superfirma", country = "DE"))