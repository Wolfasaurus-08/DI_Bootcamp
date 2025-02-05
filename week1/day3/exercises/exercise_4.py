# Exercise 4 : Disney characters
# Instructions
# Use this list :

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :
# #1/
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# #2/
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
# #3/ 
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.

disney_users_A={}
for i, name in enumerate(users):
    disney_users_A[name] = i
# for i, name in enumerate(users):
#     disney_users_A['id'] = i
#     disney_users_A['name'] = name
print (disney_users_A)
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
disney_users_B=dict(enumerate(users))
print(disney_users_B)
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
users.sort()
disney_users_C=dict(enumerate(users))
print(disney_users_C)
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.