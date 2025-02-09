#🌟 Exercise 5: For Loop
#Instructions
#Use a for loop to print all numbers from 1 to 20, inclusive.
#Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

#range (start,stop,step)
my_list=[]
for i in range(1,21):
    my_list.append(i)
print(my_list)
my_list.clear()
for i in range(1,21,2):
    my_list.append(i)
print(my_list)