str = "Hello World"
print(str)
print(type(str))    # wyświetlanie typu zmiennej
print(str[0])       # wyświetlenie pierwszego znaku zemniennej
print(str[1:4])     # wyświetlenie znaków 2-5
print(str * 3)      # zmienna razy 3
print(str + " Everyone!")   # łączenie zmiennej + dodatkowy text
print(len(str))     # ilość znaków
print(str[len(str)-1])  # wyświeltenie ostatniego znaku stringu

str2 = str + " and Hello again"     #zmienne można zapisywać w formie działań
print(str2)
print(str2[5:])     # wyświetlenie indeksu od 5 do końca
print(str2[::2])    # wyświetlenie co 3 litery stringa zaczynając zawsze od 1

print(str, end=" ")     #to zamienia znak następnej linii po princie na spację więc kolejny print będzie w tej samej linii
print(str2)
print("%-10s" % "Codenga")
#
# txt = """treść
# zmiennej
# łączona z kilku linii"""    # zamiast 3x" mozna użyć 3x'
# print(txt)
#
# text = "Pierwsza linia \n Drugalinia \t oraz tabulator \n trzecia linia w \"cudzysłowiu\" "
#
#         # zamiast dzielić text na linie można zastosować "\n" - znak nowej linii
#         # \t znak tabulacji
#         # \" znak cudzysłowia
#         # \\ znak \


# print(text)