#🌟 Exercise 4: Floats
#Instructions
#Recap – What is a float? What is the difference between an integer and a float? an integer is a whole number 
# while a float has value after the decimal point.
#reate a list containing the following sequence of floats and integers (it should be a list with mixed types):
#  1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
#Can you think of another way to generate a sequence of floats?

# float_list = [i/2 for i in range(3, 11, 1)]
# print(float_list)

my_list = []
for i in range(3,11):
    if i%2 ==0:
        my_list.append(int(i/2))
    else:
        my_list.append(i/2)

print(my_list)