year = 2100

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Year is leap")
else:
    print("Year is not leap")
