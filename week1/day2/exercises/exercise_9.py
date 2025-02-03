#Exercise 9: Cinemax
#Instructions
#A movie theater charges different ticket prices depending on a person’s age.
#if a person is under the age of 3, the ticket is free.
#if they are between 3 and 12, the ticket is $10.
#if they are over the age of 12, the ticket is $15.

#Ask a family the age of each person who wants a ticket.

#Store the total cost of all the family’s tickets and print it out.

#A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
#Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
#At the end, print the final list.

#total_price=[]
#while True:

#    age = input("How old are the members in your party? when finished type'quit' ")
    
#    if age == 'quit':
#        break
#    age=int(age)
#    if age < 3:
#        price = 0
#        total_price.append(price)
#    elif age < 12:
#      price = 10
#      total_price.append(price)
#    else:
#        price = 15
#        total_price.append(price)
#print (sum(total_price))

teen_names=["Mal ", "Zoey ", "River ", "Jayne " , "Kaylee "]
for teen in teen_names:
    teen_age = int(input(teen+"How old are you?  "))
    if teen_age>=16:
        price=15
    else:
        teen_names.remove(teen)
    
print(teen_names)
