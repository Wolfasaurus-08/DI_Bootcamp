# 🌟 Exercise 1: Cats
# Instructions
# Using this class

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
 
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
    
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


    def __repr__(self):
            return '({}, {})'.format(self.name, self.age)


cat1= Cat("Cheddar",5)
cat2= Cat("Gouda",12)
cat3= Cat("Mozzarella", 1)

cats= [cat1, cat2, cat3]

def oldest_cat(cats):
    oldest=cats[0]
    for cat in cats:
        if cat.age > oldest.age:
            oldest=cat

    return oldest

oldest = oldest_cat(cats)
print (oldest)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")


#def sortcats_age(cat):
    # return cat.age

#def sortcats_name(cat):
    # return cat.name

#sorted_cats_age= sorted(cats, key= sortcats_age)

#sorted_cats_name= sorted(cats, key= sortcats_name)
#print(cats)

#print("Object sorted by name:", sorted_cats_name)

#print("Objects sorted by age:", sorted_cats_age)