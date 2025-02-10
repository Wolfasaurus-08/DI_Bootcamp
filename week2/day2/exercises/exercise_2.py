# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
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
dog1 = Dog("Peanut", 5, 30)
dog2 = Dog("Banana", 3, 20)
dog3 = Dog("Bacon", 4, 25)
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. 
#       This method returns a string stating which dog won the fight.
#       The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.
print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(f"{dog1.name}'s running speed: {dog1.run_speed()}")
print(f"{dog2.name}'s running speed: {dog2.run_speed()}")
print(f"{dog3.name}'s running speed: {dog3.run_speed()}")

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))