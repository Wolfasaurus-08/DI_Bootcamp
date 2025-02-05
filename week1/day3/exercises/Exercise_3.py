# 
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
brand={'name':'Zara',
       'creation_date':1975,
       'creator_name': 'Amancio Ortega Gaona',
       'type_of_clothes': ['men', 'women', 'children', 'home'],
       'international_competitors': ['Gap', 'H&M', 'Benetton'],
       'number_stores': 7000,
       'major_color': {'France': 'blue', 
                       'Spain': 'red', "US": ['pink', 'green']}}
# 3. Change the number of stores to 2.
brand['number_stores']=2
# 4. Use the key [type_of_clothes] to print a sentence that explains who Zaras clients are.

# 5. Add a key called country_creation with a value of Spain.
brand['country_of_origin']='Spain'
print(brand)
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.

# 7. Delete the information about the date of creation.
brand.pop('country_of_origin')
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
US_color=brand['major_color']['US']
print(US_color)
# 10. Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))
# 11. Print the keys of the dictionary.
print(brand.keys())
# 12. Create another dictionary called more_on_zara with the following details:

more_on_zara = {'creation_date': 1975,
                'number_stores': 10000}



# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)
print(brand)
# 14. Print the value of the key number_stores. What just happened ?
print(brand['number_stores'])
#number stores updated back to 10000 because the key 'number_stores' was already there 

