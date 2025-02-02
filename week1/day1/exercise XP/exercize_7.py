#Exercise 7 : Odd or Even
#Instructions
#Write code that asks the user for a number and determines whether this number is odd or even.
num = int(input(" pick a number"))
rem = num % 2
if rem > 0:
    print ("odd")
else:
    print ("even")