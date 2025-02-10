# class Dog:  #
#     def __init__(self, name, color, breed, floppy_ears):

#         self.color=color
#         self.breed=breed
#         self.floppy_ears=floppy_ears
#     def __str__(self):
#         return f"{self.breed}, {self.color}, {self.floppy_ears}"
#     def bark(self):
#         return f"{self.name} goes WOOF!!!"
    
#     def bark (self):
#         print (f"{self.name} barks ! WAF")

#     def walk (self, number_of_meters):
#         print (f"{self.name} walked {number_of_meters} meters")
    
#     def fetch (self, object):
#         print (f"{self.name} fetched an {object}")
# peanut=Dog('brown','mutt', True) #class instance
# dingo = Dog ('white','cnaani', False)
# # class Point:
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y

# # ## create an instance of the class
# # p = Point(3,4)

# # ## access the attributes
# # print("p.x is:", p.x)
# # print("p.y is:", p.y)

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
bengal_cat = Bengal("Simba", 3)
chartreux_cat = Chartreux("Milo", 4)

print (bengal_cat.walk())