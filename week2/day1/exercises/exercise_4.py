# Exercise 4 : Afternoon at the Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     'A': "Ape",
#     'B': ["Baboon", "Bear"],
#     'C': ['Cat', 'Cougar'],
#     'E': ['Eel', 'Emu']
# }

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.animal_dict = {}

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal):
        self.animals.remove(animal)

    def sort_animals(self):
        for animal in self.animals:
            if animal[0] in list(self.animal_dict.keys()):
                self.animal_dict[animal[0]] = [self.animal_dict[animal[0]], animal]
                self.animal_dict[animal[0]].sort()
            else:
                self.animal_dict[animal[0]] = animal

        print(self.animal_dict)

    def get_groups(self, letter):
        if letter in list(self.animal_dict.keys()):
            print(self.animal_dict[letter])
        else:
            print("there are no animals of that group")

ramat_gan_safari = Zoo('fungus')

ramat_gan_safari.add_animal('calf')
ramat_gan_safari.add_animal('ape')
ramat_gan_safari.add_animal('chicken')
ramat_gan_safari.add_animal('beef')
ramat_gan_safari.add_animal('baboon')

ramat_gan_safari.get_animals()

ramat_gan_safari.sort_animals()

ramat_gan_safari.get_groups('b')
ramat_gan_safari.get_groups('t')

# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

