a_int = 1   # -> integers

a_float = 1.3645346   # -> float definition

a_string = "test"    #string is list of chars, there is no char type
a_string2 = 'test'  # " and ' are the same

print(a_string[1])

a_list = [1, 1.0, "1", [1, 2, 3]]   #mutable (can be edited), order, can be repeated
print(a_list )
a_list.append("append_test")    #dodawanie do listy
a_list[3] = 2   # zamiana indeksu
#a_list.remove("test")
del a_list[2]
print(a_list[-1])   #ostatni element z listy
print(a_list[0:3])  # wyświetlanie zakresu 1-3
print(a_list[-3:])  # 3 ostatnie elementy z listy

a_tuple = (0, 1, "2")   # z nawiasem () nieedytowalne, order, can be repeated

a_dict = {"title": "Harry potter", "author": "JK Rowling", "items": 2}  # mutable, not ordered, unique(keys)
a_dict2 = {"key": "value", 0: 1}    #int as key not recommended
print(a_dict["title"])
a_dict["items"] = 3
a_dict["cover"] = "hard"
print(a_dict)

a_set = {0, 1, 2, 1, 2}     #collection of unique values - mutable, not ordered, unique
print(a_set)

a_bool = True

if a_bool:  # false for 0, "", [], (), {}, None
   print("This is true")

print()
hobby = "sleeping"
print("I like " + hobby + " a lot")
print("I like {} a lot".format(hobby))
print(f "I like {hobby} a lot")