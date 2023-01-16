#           BREAK - przerywa działanie pętli i program kontunuuje swoją pracę za pętlą.

#           CONTINUE - przerywa aktualną iterację i od razu przechodzi do następnej

#           PASS - instrukcja pass jest pustym wypełniaczem, nic nie robi, ale stusuje sie go tam gdzie wymagane jest
#                  dodanie jakiegoś kodu np w późniejszym czasie



data = [0,1,2,3,4,5,6,7,8,9]
for v in data:
    if v == 7:
        break           # jeśli v == 7 to pętla przestaje się iterować
    print(v)
print("Dalsza część programu", "\n")


for v in data:
    if v == 3 or v == 4:
        continue        # teraz nie wyświetli sie element v=3 i 4 bo continue przechodzi do kolejnej iteracji a nie instrukcji
    print(v)
print()


if 40 > 6:
    pass                # pass tylko kompletuje instrukcję
else:
    pass
