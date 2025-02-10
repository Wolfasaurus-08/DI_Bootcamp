# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

#from exercise_2 import Dog #it imported the entire file somehow and not just the class. 

import random
class Dog:  #
    def __init__(self, name, age, weight):

        self.name = name
        self.age = age
        self.weight = weight
    def bark (self):
        return (f"{self.name} is barking")
    def run_speed(self):
        return (self.weight / self.age * 10)
    def fight(self, other_dog):
        my_strength = self.run_speed() * self.weight
        other_strength = other_dog.run_speed() * other_dog.weight
        if my_strength > other_strength:
            return (f"{self.name} won the fight")
        elif my_strength < other_strength:
            return (f"{other_dog.name} won the fight")
        else:
            return
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = ", ".join([dog.name for dog in args] + [self.name])
        print(f"{dog_names} all play together.")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
dog3 = PetDog("Rocky", 5, 30)
dog4 = PetDog("Max", 3, 20)
dog5 = PetDog("Mike", 4, 25)

dog3.train()  
dog3.play(dog4, dog5)  
dog3.do_a_trick() 