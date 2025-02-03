#Exercise 1 : Favorite Numbers
#Instructions
#Create a set called my_fav_numbers with all your favorites numbers.
#Add two new numbers to the set.
#Remove the last number.
#Create a set called friend_fav_numbers with your friend’s favorites numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
my_fav_numbers={8, 15, 9, 11, 19}
my_fav_numbers.add(4)
my_fav_numbers.add(13)
print(my_fav_numbers)
my_fav_numbers.pop()
print(my_fav_numbers)
friend_fav_numbers={ 1, 5, 8, 13, 21, 34}
our_fave_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fave_numbers)