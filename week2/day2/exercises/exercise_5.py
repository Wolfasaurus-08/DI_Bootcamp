# Exercise 5 : TheIncredibles Family
# Instructions
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore the members attributes, will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)
# Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.
# Add a method called incredible_presentation which :
# Print a sentence like “*Here is our powerful family **”
# Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)
# Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members. (did whoever make this not see the movie?)
#     [
#         {'name':'Michael','age':35,'gender':'Male','is_18':True,'power': 'fly','incredible_name':'MikeFly'},
#         {'name':'Sarah','age':32,'gender':'Female','is_18':True,'power': 'read minds','incredible_name':'SuperWoman'}
#     ]
# Call the incredible_presentation method.
# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# Call the incredible_presentation method again.




class FamilyMember:
    def __init__(self, name, age, gender, is_18):
        self.name = name
        self.age = age
        self.gender = gender
        self.is_18 = is_18

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class IncredibleMember(FamilyMember):
    def __init__(self, last_name, name, age, gender, is_18, power, incredible_name):
        super().__init__(last_name, name, age, gender, is_18)
        self.power = power
        self.incredible_name = incredible_name

    def use_power(self):
        if self.age > 18:
            print(f"{self.name}'s power is {self.power}")
        else:
            raise Exception(f"{self.name} is not over 18 years old.")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Power: {self.power}, Incredible Name: {self.incredible_name}"


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, member):
        self.members.append(member)
        print(f"Congratulations to the {self.last_name} family on the birth of {member.name}!")

    def add_member(self, member):
        self.members.append(member)
        print(f"{member.name} has joined the {self.last_name} family!")

    def family_list(self):
        print(f"The {self.last_name} family:")
        for member in self.members:
            print(member)


class TheIncredibles(Family):
    def __init__(self, last_name):
        super().__init__(last_name)

    def incredible_list(self):
        print("*Here is our powerful family*")
        super().family_list()

incredibles = TheIncredibles("Parr")

# bob = IncredibleMember('Bob Parr', 40, 'Male', True, 'Super strength', 'Mr. Incredible')
# helen = IncredibleMember('Helen Parr', 38, 'Female', True, 'Elasticity', 'Elastigirl')
# violet = IncredibleMember('Violet Parr', 14, 'Female', False, 'Invisibility', 'Violet')
# dash = IncredibleMember('Dashiell Parr', 10, 'Male', False, 'Super speed', 'Dash')
michael = IncredibleMember('Parr', 'Michael', 35, 'Male', True, 'fly', 'MikeFly')
sarah = IncredibleMember('Parr', 'Sarah', 32, 'Female', True, 'read minds', 'SuperWoman')
# incredibles.add_member(bob)
# incredibles.add_member(helen)
# incredibles.add_member(violet)
# incredibles.add_member(dash)
incredibles.add_member(michael)
incredibles.add_member(sarah)
incredibles.incredible_list()

baby_jack_jack = IncredibleMember('Jack-Jack Parr', 0, 'Male', True, 'Unknown Power', 'BabyJack-Jack')
incredibles.born(baby_jack_jack)

incredibles.incredible_list()
