# Exercise 4 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries
# last_name : (string)

# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ details.

# Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.

#     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False}

# Edited the expected output to match the assignment.

#     [
#         {'name':'Michael','age':35,'gender':'Male','is_18':True},
#         {'name':'Sarah','age':32,'gender':'Female','is_18':True}
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def add_member(self, name, age, gender, is_18):
        self.members.append({'name': name, 'age': age, 'gender': gender, 'is_18': is_18})

    def born(self, name, age, gender, is_18):
        self.add_member(name, age, gender, is_18)
        print(f"Congratulations to the {self.last_name} family on the birth of {name}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_list(self):
        print(f"The {self.last_name} family:")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}")

class RyanFamily(Family):
    def __init__(self):
        super().__init__('Ryan')

# Example usage
ryan_family = RyanFamily()
ryan_family.add_member(name='Michael', age=35, gender='Male', is_18=True)
ryan_family.add_member(name='Sarah', age=32, gender='Female', is_18=True)

ryan_family.family_list()

ryan_family.born(name='John', age=0, gender='Male', is_18=False)

ryan_family.family_list()

# Uncomment to check age
# print(ryan_family.is_18('Michael'))  # True
# print(ryan_family.is_18('John'))  # False
