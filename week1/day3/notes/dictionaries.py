#dictionaries:data structure that holds key value pairs
#   ordered and mutable

#open empty
#user_info = {'name':'ron',
             #'last_name':'Weasley',
             #'age':17,
             #'address':'ottery village-englant',
             #'family':[('arthur','father',50)('molly', 'mother', 48)],
             #'hobbies':{'quiddich', 'swimming'}}
#print(user_info['name'])
#print(user_info['family'][0])
#sample_dict = { 
#   "class":{ 
#      "student":{ 
#         "name":"Mike",
#         "marks":{ 
#            "physics":70,
#            "history":80
#         }
#      }
#   }
#}
#print(sample_dict['class']['student']['marks']['history'])
# add new value
#user_info['school']='hogwarts'
#print (user_info)
# deleting an entry
#del user_info['school]
#print(user_info)
#print ('hobbies' in user_info)
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]
for key_removie in keys_to_remove:
    if key_removie in sample_dict.keys():
        del sample_dict[key_removie]
print(sample_dict)