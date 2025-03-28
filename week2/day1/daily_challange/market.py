# Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:

# Create a class called Farm. How should it be implemented?
# Does the Farm class need an __init__ method? If so, what parameters should it take?
# How many methods does the Farm class need?
# Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# Test your code and make sure you get the same results as the example above.
class Farm:
    def __init__(self, name):
        self.name = name
        self.animal_dict = {}
       
    def add_animal(self, animal, stock=1):
        if animal in self.animal_dict:
            self.animal_dict[animal] = self.animal_dict[animal] + stock
        else:
            self.animal_dict[animal] = stock



    def get_info(self):
        for animal in self.animal_dict.keys():
            print(f"{animal} {self.animal_dict[animal]}")
        print (f" E-I-E-I-O")


macdonald = Farm("McDonald") 
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat',12)
print(macdonald.get_info())