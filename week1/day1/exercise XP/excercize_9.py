#Exercise 9 : Tall enough to ride a roller coa ster
#Instructions
#Write code that will ask the user for their height in centimeters.
#If they are over 145cm print a message that states they are tall enough to ride.
#If they are not tall enough print a message that says they need to grow some more to ride.
height=int(input("how many CM tall are you? "))
if height < 145:
    print("You need to grow up a bit before you ride thos coaster. ")
else:
    print("Enjoy the roller coaster ride")
