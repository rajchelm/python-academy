# text = "Ala ma kota "
# #
# # print(text)
# #
# # #text = text.strip()     #usuwanie spacji i innych białych znaków
# # text = text.split()  #usuwanie znaku z textu
# # #text = text.replace("a", "A")     #zamiana znaków
# # joined_text = " ".join(text)
# # print(joined_text)
# #
# # print(text)
#
# print(text.upper())
#
# text = "andrzej testowy"
# text = text.split()
# print(text)
# text = text.capitalize()

# name =
# surname =

# class User:
#     pass
# u1 = User()
# u2 = User()
# u3 = User()
#
# print(u1, u2)

# import sys
# print(sys.platform)
# print(sys.version)
#
# import random
# a = random.randint(1, 500)
# print(a)

# print(random.randint(1, 500))

# from random import randint
# print(randint(1, 100))

# class User:
#     def __init__(self, username):
#         username = username
#
#
# u1 = User('Tom')
# print(u1.username)


# age = int(input("Podaj swój wiek: "))
#
# if age >= 18:
#    print("Dorosły")
# else:
#    print("Nastolatek")


#print("|%10s|" % "?")


# class Person:
#    def __init__(self, first_name, age):
#        self.first_name = first_name
#        self.age = age
#
#    def __str__(self):
#        return "Dzień dobry. Nazywam się %s i mam %d lat!" % (self.first_name, self.age)


# class Person:
#    def __init__(self, name):
#        self.name = name
#
#    def __str__(self):
#        return "Jestem %s" % self.name
#
#
# class Worker(Person):
#    def __init__(self, name, salary):
#        super().__init__(name)
#        self.salary = salary
#
#    def __str__(self):
#        return super().__str__() + " i zarabiam %d$" % self.salary
#
#
# tom = Person("Tom")
# mike = Worker("Mike", 1200)
#
# print(tom)
# print(mike)




# class Person:
#    def __init__(self):
#        self.name = "Henryk"
#        self.surname = "Sienkiewicz"
#
#
# class Book:
#    def __init__(self):
#        self.author = Person()
#        self.book_name = "Potop"
#
#    def __str__(self):
#        return "%s %s: %s" % (self.author.name, self.author.surname, self.book_name)
#
#
# book = Book()
# print(book)



# name = "Henryk"
# surname = "Sienkiewicz"
# book_name = "Potop"
# print( "%s %s: %s" % (name, surname, book_name))



# try:
#    1/1
#    print("1")
# except ZeroDivisionError:
#    print("2")
# else:
#    print("3")
# finally:
#    print("4")



