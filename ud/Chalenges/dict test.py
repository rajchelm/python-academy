# 1. Stworz zmienną config która będzie słownikiem z konfiguracją strony internetowej,
#   zapisz w niej poniższe klucze z wartością:
#   - "website" z wartością "mysql"
#   - "dbType" z wartością "mysql"
#   - "dbUser" z wartością "admin"
#   - "dpPassword" z wartością "12345"
# 2. Pokaż ilość elementów słownika w konsoli
# 3. Pokaż w konsoli watość klucza "dbType" z słownika
# 4. Wykorzystaj pętlę for in aby przejść po wszystkich elementach słownika i pokaż je w konsoli wg formatu:
#   "Klucz w config: website z wartością example.com"



config = {
    "website" : "example.com",
    "dbType" : "mysql",
    "dbUser" : "admin",
    "dpPassword" : "12345"
}

print("Ilość elementów słownika:", len(config))

print(config["dbType"])

for key, values in config.items():
    print("Klucz w config:", key, "z wartością", values)
