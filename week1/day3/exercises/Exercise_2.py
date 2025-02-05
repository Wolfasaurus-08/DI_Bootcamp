# 🌟 Exercise 2 : Cinemax #2
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

family = {"rick": 43, 
          'beth': 13,
            'morty': 5,
              'summer': 8}


#How much does each family member have to pay ?
total_price=[]

family_names = family.keys()

for name in family_names:
    age = family[name]

    if age < 3:
        price = 0
        total_price.append(price)
    elif age < 12:
        price = 10
        total_price.append(price)
    else:
        price = 15
        total_price.append(price)
    
print (sum(total_price))

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided
# family variable (Hint: ask the user for names and ages and add them into a 
# family dictionary that is initially empty).