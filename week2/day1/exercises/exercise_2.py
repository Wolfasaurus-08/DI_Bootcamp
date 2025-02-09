# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
class Dog:
    def __init__(self, dog_name, dog_height):
        self.dog_name = dog_name
        self.dog_height = dog_height
    def bark(self,):
        print (f"{self.dog_name} goes WOOF!!!")
    def jump (self,dog_name, dog_height):
        print (f"{dog_name} jumps {2*dog_height} cm high!")
    def __str__(self):
        return f"{self.dog_name} {self.dog_height}"


davids_dog=Dog("Rex", 50)
print (davids_dog)
davids_dog.bark()
davids_dog.jump("rex", 50)
saras_dog=Dog("teacup", 20) 
dogs =[davids_dog,saras_dog]


def tallest_dog(dogs):
    tallest=dogs[0]
    for dog in dogs:
        if dog.dog_height > tallest.dog_height:
            tallest=dog

    return tallest
tallest = tallest_dog(dogs)
print (tallest)
