#for loops
#for <variable> in <iterable>
    #block of indented code

#looping in sequence
#fruits = ['apple', 'banana', 'kiwi', 'pear']

#for fruit in fruits:
 # print(fruit)

#looping in range of numbers 
#range (start,stop,step)
#for i in range(1,6):
 # print(i)
#for i in range(5):
#  print(i)
#for i in range(2,10,2):
 # print(i)

#innumerate()

#fruits = ['apple', 'banana', 'kiwi', 'pear']
#for i, fruit in enumerate(fruits):
 #if fruit==fruits[3]:
 #   print('this is the last one')
 #print(i, fruits)

#multiplication table 
num=int(input("pick a number to multiply")) 
for i in range(1,11): 
    print(num * i)