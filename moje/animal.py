class Animal:

    def make_a_sound(self):
        if animal_type = "cat":
            print("meow")
        elif animal_type == "dog":
            print("woof")
        else:
            print("no animal found")

    def calculate_food(self, weight):
        food = weight / 50
        return food

my_animal = Animal()
my_animal.make_a_sound("cat")
print(my_animal.calculate_food(100))